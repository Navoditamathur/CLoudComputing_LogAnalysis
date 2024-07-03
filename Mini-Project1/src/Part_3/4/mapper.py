#!/usr/bin/env python

import sys

for line in sys.stdin:
    # Split the line on "" to get the request
    data = line.strip().split('"')
    # if it has 3 parts atleast (has 9 including spaces)
    if len(data) > 2:
        # Split the 2nd part on ' ' to get request method, URL, and HTTP version 
        request = data[1].split(' ')
        if len(request) > 2:
            # get the path
            path = request[1]
            print(path + "\t" + str(1))
