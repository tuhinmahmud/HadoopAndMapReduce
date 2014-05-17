#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import re
def is_valid(word):
    if word =="":
        return False
    return True

i =0
for line in sys.stdin:
    ##print line
    data = re.split(r'[\s|\.|\?|!|:|;|"|\(|\)|<|>|\[|\]|#|\$|=|-|/|,]+',line)
    #data = re.split(r'[\s|"]+',line)
    #print data
    #if i >= 10:
    #    break;
    for word in data:
        if is_valid(word):
            print "{0}\t{1}".format(word.lower(),i)
    i = i + 1
    
