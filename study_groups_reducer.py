#!/usr/bin/python
import sys
import csv
reader = csv.reader(sys.stdin, delimiter='\t')
def reducer():
	authorList = []
	oldKey = None
        i=0
	for line in reader:
            i +=1
            if len(line) == 0:
                continue
	    thisKey ,thisAuthor, thisType = line
	    if oldKey and thisKey != oldKey:
		 print "{0}\t{1}".format(oldKey,authorList)
                 authorList =[]

	    oldKey = thisKey
            authorList.append(thisAuthor)
	if oldKey !=None:
	    print "{0}\t{1}".format(oldKey,authorList)
reducer()
