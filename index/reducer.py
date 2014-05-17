#!/usr/bin/python

import sys

i = 0
oldKey = None
nodeSet= set()
nodeList = []

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        print "skipping as data_mapped is wrong ",data_mapped 
        continue

    thisKey, thisNode = data_mapped
    #print "\t\t\t",thisKey, "\t", thisNode,"\t",count

    if oldKey and thisKey != oldKey:
        nodeList= list(nodeSet)
        nodeList.sort()
        #print nodeList
        print oldKey, "\t",','.join(str(x) for x in nodeList)
        nodeSet.clear()
        del nodeList[:]
    i += 1
    oldKey = thisKey
    nodeSet.add(thisNode)

if oldKey !=None:
    nodeList= list(nodeSet)
    nodeList.sort()
    #print nodeList
    print oldKey, "\t",','.join(str(x) for x in nodeList)

