#!/usr/bin/python
import sys
import csv
reader = csv.reader(sys.stdin, delimiter='\t')
def reducer():
	authorList = [] #author list for post
	oldKey = None
        i=0
	for line in reader:
            i +=1
            if len(line) == 0:
                continue
	    thisKey ,thisAuthor, thisType = line
            #for a new key in the sorted <key,value> pair
            # output the authorList for this key and reset authorlist for next
	    if oldKey and thisKey != oldKey:
		 print "{0}\t{1}".format(oldKey,authorList)
                 authorList =[]

	    oldKey = thisKey
            #add to the list of authors
            authorList.append(thisAuthor)
	if oldKey !=None:
	    print "{0}\t{1}".format(oldKey,authorList)
reducer()
