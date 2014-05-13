#!/usr/bin/python

import sys
import re
import csv
import time
import datetime
#import xml.utils.iso8601
#import dateutil.parser
reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
def mapper():
	i=0
	for line in reader:
	    i+=1
	    #if i == 1:
	    #   continue
	    if len(line) < 9:
		continue
            id  = line[0]
            node_type  = line[5]
            abs_parent_id  = line[7]
            body =line[4]
            author_id =line[3]
            if node_type == "question":
	        writer.writerow([id,author_id,node_type])
            if node_type == "answer":
	        writer.writerow([abs_parent_id,author_id,node_type])
mapper()
		
