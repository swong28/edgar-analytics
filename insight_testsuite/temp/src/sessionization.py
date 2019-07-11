from collections import OrderedDict
from datetime import datetime, timedelta

from session import Session

def readLogs(filename, INACT_TIME, outputFile):
    '''
    (str, timestamp, str) -> None

    Process input files with out 
    '''

    # format for datetime object
    FORMAT = '%Y-%m-%d %H:%M:%S'

    # time dict and queue
    sessionDict = OrderedDict()

    # Read EDGAR Log
    with open(filename, 'r') as txt:
        for idx, line in enumerate(txt):
            # Skip Header
            if (idx == 0):
                continue

            # Get needed information
            data = line.split(',')
            ip, date, time = data[:3]

            # Format Date and Time Columns
            try:
                accessTime = datetime.strptime(date + ' ' + time, FORMAT)
            except:
                print("date or time is not in the correct format.")
                continue

            # write to output if passed inactivity period
            removed_list = []
            for temp_ip, session in sessionDict.items():
                if session.isExpired(accessTime):
                    writeOutput(outputFile, str(session))
                    removed_list.append(temp_ip)

            for item in removed_list:
                sessionDict.pop(item)

            # Put Record in sessionDict
            if ip not in sessionDict:
                sessionDict[ip] = Session(ip, accessTime, INACT_TIME)
            else:
                sessionDict[ip].updateEndTime(accessTime)
    
    # Assume all records as ex
    writeAll(outputFile, sessionDict)

def getInactivityPeriod(inactFile):
    '''
    str -> num

    Return the inactivity period from the inactivity file.
    '''
    f = open(inactFile)
    INACT_TIME = f.readline()
    f.close()

    return timedelta(seconds=int(INACT_TIME))

def writeOutput(outputFile, output):
    '''
    '''
    f = open(outputFile, "a")
    f.write(output+'\n')
    f.close()

def writeAll(outputFile, sessions):
    '''
    '''
    f = open(outputFile, "a")
    for _ip, session in sessions.items():
        f.write(str(session)+'\n')
    f.close()

if __name__ == '__main__':
    from sys import argv
    inputFile, inactFile, outputFile = argv[1:]

    INACT_TIME = getInactivityPeriod(inactFile)
    readLogs(inputFile, INACT_TIME, outputFile)