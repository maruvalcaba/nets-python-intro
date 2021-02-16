#! /usr/bin/env python3

import os
import re
import sys

inputfile = sys.argv[1]
outfile = sys.argv[2]
file1 = open(inputfile, 'r')
wordDict = dict()
for line in file1:
    line = line.strip()
    line = line.lower()
    words = re.split('[^\w]',line)
    for word in words:
        if word in wordDict:
            wordDict[word] = wordDict[word]+1
        else:
            wordDict[word] = 1
file2 = open(outfile, 'w')
for key in sorted(wordDict):
    if len(key) > 0:
        line = key+ ' '+str(wordDict[key])+"\n"
        file2.write(line)
file1.close()
file2.close()
    
