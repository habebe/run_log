class AgentLogParser:
    def __init__(self):
        pass
    def parseMessage(self,line):
        end = line.find("]")
        if end != -1:
            start = line.find("[")
            if start != -1:
                timestamp = line[start+1:end].strip()
                message   = line[end:]
                message   = message[message.find(":")+1:].strip()
                return (timestamp,message)
            pass
        return None
    pass

class UpsertAgentLogParser(AgentLogParser):
    def __init__(self):
        self.preProcessTimeStamp = [None,None]
        self.processTimeStamp    = [None,None]
        self.preProcessCounter = 0
        self.processCounter = 0
        self.pre_data = {}
        self.prc_data = {}
        pass
    
    def parse(self,line):
        data = self.parseMessage(line)
        if data != None:
            message = data[1]
            data = message.split(",")
            if (data != None) and len(data) >= 4:
                T = data[0].strip()
                if T == "U":
                    type = int(data[1])
                    timestamp = float(data[2])
                    counter = float(data[3])
                    if type == 0:
                        self.pre_data[counter] = [timestamp,0]
                        if self.preProcessTimeStamp[0] == None:
                            self.preProcessTimeStamp[0] = timestamp
                            pass
                        self.preProcessTimeStamp[1] = timestamp
                        self.preProcessCounter = counter
                    elif type == 1:
                        if self.pre_data.has_key(counter):
                            self.pre_data[counter] = [self.pre_data[counter][0],timestamp]
                            pass
                        if self.processTimeStamp[0] == None:
                            self.processTimeStamp[0] = timestamp
                            pass
                        self.processTimeStamp[1] = timestamp
                        self.processCounter = counter
                        pass
                    elif type == 2:
                        self.prc_data[counter] = timestamp
                    elif type == 3:
                        if self.prc_data.has_key(counter):
                            self.prc_data[counter] = (timestamp - self.prc_data[counter])
                            pass
                    return True
                    pass
                pass
            pass
        return False
    pass

import sys
f = file(sys.argv[1],"r")
line = f.readline()
parser = UpsertAgentLogParser()
while len(line):
    parser.parse(line)
    line = f.readline()
    pass

f = file("agent.preprocess.time","w")
sum_pre = 0
counter_pre = 0
sample_rate = 10000
counter = 0
for i in parser.pre_data.keys():
    data = parser.pre_data[i]
    if data[1] != 0:
        t = (data[1]-data[0])
        sum_pre += t
        counter_pre += 1
        counter += 1
        if counter_pre == sample_rate:
            print >>f,counter,",",sum_pre/sample_rate
            counter_pre = 0
            sum_pre = 0
        pass
    pass


    
f = file("agent.process.time","w")
sum_pre = 0
counter_pre = 0
sample_rate = 10000
counter = 0
for i in parser.prc_data.keys():
    data = parser.prc_data[i]
    if data[1] != 0:
        t = (data[1]-data[0])
        sum_pre += t
        counter_prc += 1
        counter += 1
        if counter_prc == sample_rate:
            print >>f,counter,",",sum_prc/sample_rate
            counter_prc = 0
            sum_prc = 0
        pass
    pass


