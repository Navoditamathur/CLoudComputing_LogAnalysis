#!/usr/bin/env python

import sys

for line in sys.stdin:
    # Split the line to get the ip
    data = line.strip().split(' ')
    if len(data) > 1:
        # get ip address
        ip = data[0].strip()
        print(ip + "\t" + str(1))
