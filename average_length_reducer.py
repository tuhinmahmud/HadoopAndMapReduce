#!/usr/bin/python
import sys
import csv
reader = csv.reader(sys.stdin, delimiter='\t')
def reducer():
	count = 0
	oldKey = None
        aLen =0
        qLen =-1
        ansCnt =0
        avgLen =0
	for line in reader:
            if len(line) == 0:
                continue
	    thisKey ,thisLen, thisType = line
	    if oldKey and thisKey != oldKey:
                 if ansCnt > 0:
			 avgLen = float(aLen)/ansCnt
                 if qLen >=0 :
			 print "{0}\t{1}\t{2}".format(oldKey,qLen,avgLen)
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
