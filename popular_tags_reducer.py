#!/usr/bin/python
import sys
import csv
import operator
reader = csv.reader(sys.stdin, delimiter='\t')
def reducer():
        tagDict ={} # used for holding the tag counts
	count = 0  # count of a  tag

	oldKey = None
        i=0
	for line in reader:
            i +=1
            #don't consider empty line
            if len(line) == 0:
                continue
	    thisKey ,thisLen = line

	    if oldKey!=None and thisKey != oldKey:
                 #update dictionary for tag count and reset the current count
                 tagDict[oldKey] = count;
                 count =0

	    oldKey = thisKey
            count +=1

	if oldKey !=None:
	    tagDict[oldKey] = count;
        
        #sort the tag dictionary according to the count values in reverse order
        sorted_tags = sorted(tagDict.iteritems(), key=operator.itemgetter(1),reverse=True)
        i =0 
        for k, v in sorted_tags:
           #only output the first 10 entry
           if i > 9:
              break
           print k, v
           i +=1
        
reducer()
