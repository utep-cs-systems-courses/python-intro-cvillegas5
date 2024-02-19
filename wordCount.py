#! /usr/bin/env python3

import os
import re
import sys
import subprocess


if len(sys.argv) is not 4:
    exit()

textFname = sys.argv[1]
inputFile = sys.argv[2]


#fd = os.open(sys.argv[2], os.O_RDONLY)

master = {}

with open(inputFile, 'r') as inputFile:
    for line in inputFile:
        line = line.strip()
        #splits from multiple word boundary delimiters
        word = re.split(r"[\b\W\b]+", line.lower())
        for x in word:
            if x in master:
                master[x] += 1
            else:
                master[x] = 1

fd = os.open(sys.argv[3], os.O_WRONLY | os.O_CREAT)
for key, value in master.items():
    newLine = str(key) + " " + str(value)
    os.write(fd, newLine)

os.close(fd)
