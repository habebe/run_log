def read(fileName,type):
    f = file(fileName,"r")
    line = f.readline()
    data = []
    while len(line):
        point = eval(line)
        data.append([point["data"][type],point["data"]["rate"]])
        line = f.readline()
        pass
    return data


import sys

data = read(sys.argv[1],sys.argv[2])
f = file("{0}.data".format(sys.argv[1]),"w")
favg = file("{0}.average".format(sys.argv[1]),"w")
counter = 0
total = 0
for i in data:
    counter += i[0]
    total += i[1]
    print >>f,counter,",",i[1]
    pass
print total/len(data)
total = (total/len(data))
print >> favg,"0,{0}".format(total)
print >> favg,"{0},{1}".format(counter,total)

    
