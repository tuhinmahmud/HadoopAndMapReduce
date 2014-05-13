#!/usr/bin/python
import sys
import csv
import operator
reader = csv.reader(sys.stdin, delimiter='\t')
def reducer():
        tagDict ={}
	count = 0
	oldKey = None
        i=0
	for line in reader:
            i +=1
            if len(line) == 0:
                continue
	    thisKey ,thisLen = line

	    if oldKey!=None and thisKey != oldKey:
                 tagDict[oldKey] = count;
                 count =0

	    oldKey = thisKey
            count +=1

	if oldKey !=None:
	    tagDict[oldKey] = count;
        sorted_tags = sorted(tagDict.iteritems(), key=operator.itemgetter(1),reverse=True)
        i =0 
        for k, v in sorted_tags:
           if i > 9:
              break
           print k, v
           i +=1
        
reducer()
