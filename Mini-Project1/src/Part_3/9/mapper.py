#!/usr/bin/env python

import sys

for line in sys.stdin:
  # Split the line on "" to get the data
  data = line.strip().split('"')
  # if it has 3 parts atleast
  if len(data) > 2:
    # get ip 
    ip_part = data[0].strip().split(' ')
    if len(ip_part) > 1:
        ip = ip_part[0]
        # get status_part
        size_part = data[2].strip().split(' ')
        if len(size_part) > 1:
            size = size_part[1].strip()
            print(ip +"\t1\t"+ size)