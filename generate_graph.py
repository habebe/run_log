import os
import sys

def get_listing():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"log")
    _listing = os.listdir(path)
    listing = []
    for i in _listing:
        listing.append(os.path.join(path,i))
        pass
    return listing
                        

def read(fileName):
    f = file(fileName,"r")
    line = f.readline()
    data = []
    while len(line):
        point = eval(line)
        data.append([point["data"]["C"],point["data"]["rate"]])
        line = f.readline()
        pass
    return data


dataset = {}
for i in get_listing():
    data = read(i)
    counter = 0
    f = file(os.path.basename(i)+".profile","w")
    counter = 0
    xCounter = 0
    for j in data:
        counter += j[0]
        xCounter += j[0]
        print >>f,counter,",",j[1]
        D = [0,0]
        if dataset.has_key(xCounter):
            D = dataset[xCounter]
            pass
        D[0] += j[0]
        D[1] += j[1]
        dataset[xCounter] = D
        pass
    f.close()
    pass

print dataset
length = len(dataset)
counter = 0
f = file("overall.txt","w")
keys = dataset.keys()
keys.sort()
for i in keys:
    counter = dataset[i][0]
    print >>f,i,",",dataset[i][1]
    pass
f.close()
