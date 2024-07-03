#!/usr/bin/env python

import sys

for line in sys.stdin:
    # Split the line on "" to get the request
    data = line.strip().split('"')
    # if it has 3 parts atleast
    if len(data) > 2:
        # Split the 2nd part on ' ' to get request method, URL, and HTTP version
        request = data[1].split(' ')
        if len(request) > 2:
            # get the url
            url = request[1].strip()
            # If "/images/smilies/" is url, print it to output stream
            if "/images/smilies/" in url:
                print("hits\t" +str(1))