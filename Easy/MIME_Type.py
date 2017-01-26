import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(raw_input())  # Number of elements which make up the association table.
q = int(raw_input())  # Number Q of file names to be analyzed.
dic=dict()


#creation of a dictionnary : "ext:mt"
for i in xrange(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = raw_input().split()
    dic[ext.lower()]=mt


for i in xrange(q):
    fname = raw_input()# One file name per line.
    fname2=fname.lower()#case insensitive
    lon=len(fname2)
    fna=[i for i in fname]
    fna2=fna[::-1]


    #thanks to the reversed list, i can find the index of the extension
    if "."in fna2:
        t=lon-fna2.index(".")
    else:
        print "UNKNOWN"
        continue

    #if the extension if in my dictionnary, just need to call it, else: unknown
    if fname2[t:lon] in dic.keys():
        print dic[fname2[t:lon]]
    else:
        print "UNKNOWN"
