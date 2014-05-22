#!/usr/bin/python
import sys
import csv
reader = csv.reader(sys.stdin, delimiter='\t')
def reducer():
	count = 0
	oldKey = None
        maxHour =0
        maxHourCnt =0
        i=0
        counters ={} #dictionary for maximum counts for a given hour
        hourList =[] # list of hour corresponding to student ..can have duplicate entries
	for line in reader:
 
            i +=1
            if len(line) == 0:
                continue
	    thisKey ,thisHour = line
	    if oldKey and thisKey != oldKey:
                 uniqueHour={} # a dictionary of unique hours
                 for hour in hourList:
                     # if this hour has the maximum count add to uniqueHour 
                     # if it is not already there
                     if counters[hour] == maxHourCnt:
                         if hour not in uniqueHour:
                             uniqueHour[hour]=hour
                 #output the key and unihour that has maxCount
                 for key, value in uniqueHour.iteritems() :
		     print "{0}\t{1}".format(oldKey,value)
                 #reset for the next 
                 counters = {}
                 maxHour =0
                 maxHourCnt=0
                 hourList=[]

	    oldKey = thisKey
            hourList.append(thisHour)
            #counters updated to keep track of couts of post in thisHour
            if thisHour in counters:
		counters[thisHour] +=1
            else:
		counters[thisHour]=1
            #update the maxHourCnt and the corresponding maxHour
            if maxHourCnt < counters[thisHour]:
                 maxHourCnt = counters[thisHour]
                 maxHour = thisHour
            
	if oldKey !=None:
                 uniqueHour={}
                 for hour in hourList:
                     if counters[hour] == maxHourCnt:
                         if hour not in uniqueHour:
                             uniqueHour[hour]=hour
                 for key, value in uniqueHour.iteritems() :
		     print "{0}\t{1}".format(oldKey,value)
reducer()
