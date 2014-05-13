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
	for line in reader:
	    if len(line) < 9:
		continue
            tags  = line[2].split(" ")
            node_type = line[5]
            if node_type == "question" or node_type == "answer" or  node_type == "comments" :
		    for tag in tags:
                        if tag !='':
			    writer.writerow([tag,1])
mapper()
		
