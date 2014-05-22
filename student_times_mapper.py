#!/usr/bin/python

import sys
import re
import csv
import time
import datetime
reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
""" mapper routine to output student and timestamp hour pairs"""
def mapper():
	for line in reader:
	    if len(line) < 9:
		continue
            try :
                mydate = time.strptime(line[8], '%Y-%m-%d %H:%M:%S.%f+00')
            except:
		continue
            else:
                myhour = mydate.tm_hour
                #output studentid and hour of the post
	        writer.writerow([line[3],myhour])
mapper()
		
