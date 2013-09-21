from collections import deque
 
class SMA():
    def __init__(self, period):
        assert period == int(period) and period > 0, "Period must be an integer >0"
        self.period = period
        self.stream = deque()
        pass

    def __call__(self, n):
        stream = self.stream
        stream.append(n)    # appends on the right
        streamlength = len(stream)
        if streamlength > self.period:
            stream.popleft()
            streamlength -= 1
            pass
        if streamlength == 0:
            average = 0
        else:
            average = sum( stream ) / streamlength
            pass
        return average

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
        self.c0 = 0
        self.c1 = 0
        self.c2 = 0
        self.c3 = 0
        self.profile = {}
        self.connect_map = {}
        self.idle_time = []
        self.idle_start_time = None
        self.start_time = None
        self.stop_time = None
        pass
    
    def get_start_time(self):
        return self.start_time
    
    def get_stop_time(self):
        start_time = self.stop_time.split("|")[2].split(":")
        start_time = (int(start_time[0])*60 + int(start_time[1]) + float(start_time[2])/60.0)
        print "Stop time:",start_time
        return start_time

    def parse(self,line):
        log_data = self.parseMessage(line)
        if log_data != None:
            message = log_data[1]
            data = message.split(",")
            if (data != None) and len(data) >= 3:
                if self.start_time == None:
                    start_time = log_data[0].split("|")[2].split(":")
                    start_time = (int(start_time[0])*60 + int(start_time[1]) + float(start_time[2])/60.0)
                    self.start_time = start_time
                    print "Start time (minutes):",self.start_time
                    pass
                self.stop_time = log_data[0]
                T = data[0].strip()
                P = None
                if not self.profile.has_key(T):
                    self.profile[T] = []
                    pass
                P = self.profile[T]
                D = []
                for i in xrange(1,len(data)):
                    D.append(float(data[i]))
                    pass
                P.append(D)
                if self.idle_start_time:
                    stop_time = log_data[0].split("|")[2].split(":")
                    start_time = self.idle_start_time.split(":")
                    start_time = (int(start_time[0])*60 + int(start_time[1]) + float(start_time[2])/60.0)
                    stop_time  = (int(stop_time[0])*60 + int(stop_time[1]) + float(stop_time[2])/60.0)
                    diff = stop_time - start_time
                    print "Idle {0} minutes ({1})".format(diff,log_data[0].split("|")[2])
                    self.idle_time.append(diff)
                    self.idle_start_time = None
                    pass
                pass
            elif message == "No pipeline work found... agent idle":
                if self.idle_start_time == None:
                    self.idle_start_time = log_data[0].split("|")[2]
                    pass
                pass
            pass
        return False
    pass

import sys
f = file(sys.argv[1],"r")
line = f.readline()
parser = UpsertAgentLogParser()
counter = 0
limit = -100000
while len(line):
    parser.parse(line)
    line = f.readline()
    if limit > 0 and counter > limit:
        line = ""
        pass
    counter += 1
    pass

import os

def process_idle_time(parser):
    f = file("idle.time","w")
    counter = 0
    total = 0
    for i in parser.idle_time:
        counter += 1
        print >> f,"{0},{1}".format(counter,i) 
        total += i
        pass
    print "Total idle time:{0} counter:{1}".format(total,counter)
    print "Total time {0}".format(parser.get_stop_time()-parser.get_start_time())
    pass

def process_time(fileName,profile,key,sample_rate=1000,sma_period=10):
    if not profile.has_key(key):
        return
    data = profile[key]
    f = file(fileName,"w")
    counter = 0
    total = 0
    total_counter = 0
    f_sma = file("{0}.sma.{1}".format(fileName,sma_period),"w")
    sma = SMA(sma_period)
    overall_total = 0
    overall_counter = 0
    for i in data:
        time = i[0]
        counter += 1
        total_counter += 1
        overall_counter += 1
        overall_total += time 
        total += time
        if(total_counter % sample_rate) == 0:
            T = (total*1e-6/sample_rate)
            print >> f,"{0},{1}".format(counter,T)
            print >> f_sma,"{0},{1}".format(counter,sma(T))
            total = 0
            total_counter = 0
            pass
        pass
    average = (overall_total*1e-6)/overall_counter
    f_avg = file("{0}.average".format(fileName),"w")
    print >> f_avg,"{0},{1}".format(sample_rate,average)
    print >> f_avg,"{0},{1}".format(overall_counter,average)
    pass

def process_rate(fileName,profile,key,sample_rate=1000,sma_period=10):
    if not profile.has_key(key):
        return
    data = profile[key]
    f = file(fileName,"w")
    counter = 0
    total = 0
    total_counter = 0
    f_sma = file("{0}.sma.{1}".format(fileName,sma_period),"w")
    sma = SMA(sma_period)
    overall_total = 0
    overall_counter = 0
    for i in data:
        time = i[0]
        counter += 1
        total_counter += 1
        total += time
        overall_total += time
        overall_counter += 1
        if(total_counter % sample_rate) == 0:
            T = sample_rate*1e9/(total)
            print >> f,"{0},{1}".format(counter,T)
            print >> f_sma,"{0},{1}".format(counter,sma(T))
            total = 0
            total_counter = 0
            pass
        pass
    average = (overall_counter*1e9)/(overall_total)
    f_avg = file("{0}.average".format(fileName),"w")
    print >> f_avg,"{0},{1}".format(sample_rate,average)
    print >> f_avg,"{0},{1}".format(overall_counter,average)

    pass

def process_connectivity(fileName,profile,key):
    if not profile.has_key(key):
        return
    data = profile[key]
    
    c_map = {}
    for i in data:
        time = i[0]
        connections = i[2]
        if not c_map.has_key(connections):
            c_map[connections] = [time]
        else:
            c_map[connections].append(time)
            pass
        pass
    keys = c_map.keys()
    keys.sort()
    f_count = file("{0}.connection.hist".format(fileName),"w")
    f_time = file("{0}.connection.time.hist".format(fileName),"w")
    for i in keys:
        items = c_map[i]
        length = len(items)
        print >> f_count,i,",",length
        S = sum(items)*1e-6/length
        print >> f_time,i,",",S
        pass
    pass

process_idle_time(parser)

process_connectivity("web",parser.profile,"C")

process_time("task.preprocess.time",parser.profile,"A")
process_time("task.process.time",parser.profile,"B")
process_time("subtask.preprocess.time",parser.profile,"D")
process_time("subtask.connectivity.time",parser.profile,"C")
process_time("subtask.process.query.time",parser.profile,"E")
process_time("subtask.process.time",parser.profile,"F")


process_rate("task.preprocess.rate",parser.profile,"A")
process_rate("task.process.rate",parser.profile,"B")
process_rate("subtask.preprocess.rate",parser.profile,"D")
process_rate("subtask.connectivity.rate",parser.profile,"C")
process_rate("subtask.process.query.rate",parser.profile,"E")
process_rate("subtask.process.rate",parser.profile,"F")




