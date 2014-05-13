#!/usr/bin/python

import sys
import re
import csv
import time
import datetime
reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
def mapper():
	for line in reader:
	    if len(line) < 9:
		continue
            id  = line[0]
            node_type  = line[5]
            abs_parent_id  = line[7]
            body =line[4]
            if node_type == "question":
	        writer.writerow([id,len(body),node_type])
            if node_type == "answer":
	        writer.writerow([abs_parent_id,len(body),node_type])
mapper()
		
