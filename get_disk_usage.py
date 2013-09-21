import os

def usage(disk):
    os.system("du -h {0}/*".format(disk))
    pass

for i in xrange(2,7):
    disk = "/data{0}/ig.data/".format(i)
    usage(disk)
    pass
