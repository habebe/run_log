import os
import csv

def average(fileName):
    f = file(fileName,"r")
    f_out = file("{0}.average".format(fileName),"w")
    line = f.readline()
    total = 0
    counter = 0
    start = None
    end = None
    min_value = None
    max_value = None
    while len(line):
        data = line.split(",")
        if start == None:
            start = data[0]
            min_value = float(data[1])
            max_value = float(data[1])
            pass
        end = data[0]
        data = float(data[1])
        min_value = min(data,min_value)
        max_value = max(data,max_value)
        total += data
        counter += 1
        line = f.readline()
        pass
    average = 0
    if counter > 0:
        average = total*1.0/counter
        pass
    print fileName,"total : {0} counter : {1} average:{2} range({3},{4})".format(total,counter,average,min_value,max_value)

    print >> f_out,start,",",average
    print >> f_out,end,",",average
    pass


listing = os.listdir(".")
for i in listing:
    if i.endswith(".time"):
        average(i)
    elif i.endswith(".rate"):
        average(i)
        pass
    pass
