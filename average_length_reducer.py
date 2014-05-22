#!/usr/bin/python
import sys
import csv
reader = csv.reader(sys.stdin, delimiter='\t')
def reducer():
	count = 0
	oldKey = None
        aLen =0 # running sum of the length values
        qLen =-1
        ansCnt =0 # running count of entries
        avgLen =0 # average lenght for a given key from the < key, len > pair
	for line in reader:
            if len(line) == 0:
                continue
	    thisKey ,thisLen, thisType = line
            # if the key value changes in the sorted list
            # find the average of the Len and reset 
	    if oldKey and thisKey != oldKey:
                 #making sure there are some answers
                 if ansCnt > 0:
			 avgLen = float(aLen)/ansCnt
                 # making sure there is a question corresponding the answers
                 if qLen >=0 :
			 print "{0}\t{1}\t{2}".format(oldKey,qLen,avgLen)
                 #reset loop values for next key 
                 aLen =0
                 qLen =-1
                 ansCnt =0

	    oldKey = thisKey
            if thisType =="question":
                   qLen = thisLen
            if thisType =="answer":
                  aLen += int(thisLen)
                  ansCnt +=1

	if oldKey !=None:
                 avgLen =0
                 if ansCnt > 0:
			 avgLen = aLen /ansCnt
                 if qLen >=0 :
			 print "{0}\t{1}\t{2}".format(oldKey,qLen,avgLen)
reducer()
