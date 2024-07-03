#!/usr/bin/env python

import sys

for line in sys.stdin:
    # Split the line to get the ip
    data = line.strip().split(' ')
    # get ip addr
    ip = data[0].strip()
    if ip == "96.32.128.5":
        print("hits\t" +str(1))
