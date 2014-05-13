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
        counters ={}
        hourList =[]
	for line in reader:
 
            i +=1
            if len(line) == 0:
                continue
	    thisKey ,thisHour = line
	    if oldKey and thisKey != oldKey:
                 uniqueHour={}
                 for hour in hourList:
                     if counters[hour] == maxHourCnt:
                         if hour not in uniqueHour:
                             uniqueHour[hour]=hour
                 for key, value in uniqueHour.iteritems() :
		     print "{0}\t{1}".format(oldKey,value)
                 counters = {}
                 maxHour =0
                 maxHourCnt=0
                 hourList=[]
	    oldKey = thisKey
            hourList.append(thisHour)
            if thisHour in counters:
		counters[thisHour] +=1
            else:
		counters[thisHour]=1
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
