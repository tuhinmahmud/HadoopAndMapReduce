#!/usr/bin/python

import sys
import re
import csv
import time
import datetime

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

""" mapper routine that outputs <key,value> pairs for each line
of input key=tag and value=1. These are used in reducer for tag count"""
def mapper():
	for line in reader:
            #filter out lines not formated correctly
	    if len(line) < 9:
		continue
             
            tags  = line[2].split(" ")
            node_type = line[5]
            # only use the tags for entries with nodetype 'question' or 'answer' or 'comments'
            if node_type == "question" or node_type == "answer" or  node_type == "comments" :
		    for tag in tags:
                        #don't consider empty tag
                        if tag !='':
			    writer.writerow([tag,1])
mapper()
		
