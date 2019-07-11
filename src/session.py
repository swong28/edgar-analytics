from datetime import datetime

class Session:
    def __init__(self, ip, accessTime, inactivityPeriod):
        self.ip = ip
        self.startTime = accessTime
        self.endTime = accessTime
        self.inactivityPeriod = inactivityPeriod
        self.record = 1
        self.FORMAT = '%Y-%m-%d %H:%M:%S'
    
    def isExpired(self, currentTime):
        return ((self.endTime + self.inactivityPeriod) < currentTime)
    
    def updateEndTime(self, accessTime):
        self.endTime = accessTime
        self.record += 1
    
    def calculateTotalTime(self):
        totalTime = (self.endTime - self.startTime).total_seconds() + 1
        return str(int(totalTime))
    
    def __str__(self):
        startTime = datetime.strftime(self.startTime, self.FORMAT)
        endTime = datetime.strftime(self.endTime, self.FORMAT)
        totalTime = self.calculateTotalTime()
        record = str(self.record)
        return "{},{},{},{},{}".format(self.ip, startTime, endTime, totalTime, record)

