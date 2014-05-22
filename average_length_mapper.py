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
            #filter out lines that are not all the required fields 
	    if len(line) < 9:
		continue
            #collect values of id, node_type, abs_parent_id and body from each line 
            id  = line[0]
            node_type  = line[5]
            abs_parent_id  = line[7]
            body =line[4]
            # depending if the line entry corresponds to a question or an answer 
            # maper outputs first field accordingly so that the question and corresponding answers 
            # are grouped by the same id for the reducer 
            if node_type == "question":
	        writer.writerow([id,len(body),node_type])
            if node_type == "answer":
	        writer.writerow([abs_parent_id,len(body),node_type])
mapper()
		
