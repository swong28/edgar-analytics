# Problem Statement

Many people use Exchange Commission's Electronic Data Gathering, Analysis and Retrieval (EDGAR) system to retrieve financial documents. The problem here is to build a pipeline to ingest that stream of data and calculate how long a particular user spends on EDGAR during a visit and how many documents that user requests during the session.

# Assumption
Here are some assupmtions for this coding challenge:

    1. Each IP address represents a single user.
    2. Each entry counts as an unique request.
    3. Any invalid entry will be ignored, such as datetime with wrong format.
    4. Data size can fit into memory.

# Solution

I decided to build my code with Session object to keep track of the expiration time of the session. And since the output of the data depends on the ordering of input and expiration time, OrderedDict datatype is used to store these Session objects. OrderedDict has the advantages of O(1) runtime for get item, set item, and delete item while maintaining the inserting orders.

When reading an input file, the file will be read line by line. Then the ip address, date, and time will be extracted each line. Then, the date and time will use to check if existing sessions in the orderedDict has expired and write the expired sessions to output. After checking all of the existing sessions in OrderedDict, new session will be updated or created based on if the ip adress is already in the OrderedDict. When the all the input file lines are completed process, all sessions in the OrderedDict will be assumed expired and written to output file.

# Future Plan
For scaling and when data size become larger, I recommend implementing Apache Kafka to stream data for high-throughput and ow latency. Apache Kafka can ingest real-time data and detect any abnormalty in users easily. 