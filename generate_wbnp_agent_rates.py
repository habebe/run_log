import os
import sys

def get_average(file_name):
    f = file(file_name,"r")
    line = f.readline()
    line = f.readline()
    data = line.split(",")
    data = [float(data[0]),float(data[1])]
    return data

def collect_averages(map,dirname):
    listing = os.listdir(dirname)
    dirs = []
    for i in listing:
        if i.endswith(".average"):
            if i.find("rate") > 0:
                if map.has_key(i):
                    map[i].append(os.path.join(dirname,i))
                else:
                    map[i] = [os.path.join(dirname,i)]
                    pass
                pass
            pass
        pass
    pass

def process_files(root,key,files):
    f = file(os.path.join(root,key),"a")
    rate = 0
    W = 0
    print key,len(files)
    for i in files:
        print "\t",get_average(i)
        data = get_average(i)
        #rate += get_average(i)
        W += data[0]
        rate += (data[0]*data[1])
        pass
    weighted_average = rate/W
    rate = weighted_average*len(files)
    print "Overall",rate
    print >> f,len(files),",",rate
    f.close()
    pass


def process_top_dir(root,dirname):
    listing = os.listdir(dirname)
    dirs = []
    for i in listing:
        if i.startswith("agent."):
            if i.endswith(".initial"):
                dirs.append(os.path.join(dirname,i))
                pass
            pass
        pass
    map = {}
    for i in dirs:
        collect_averages(map,i)
        pass
    for i in map:
        process_files(root,i,map[i])
        pass
    pass


process_top_dir("./wbnp.agents.data","./wbnp.agents/agent.size.1")
process_top_dir("./wbnp.agents.data","./wbnp.agents/agent.size.2")
process_top_dir("./wbnp.agents.data","./wbnp.agents/agent.size.3")
process_top_dir("./wbnp.agents.data","./wbnp.agents/agent.size.4")
process_top_dir("./wbnp.agents.data","./wbnp.agents/agent.size.5")

