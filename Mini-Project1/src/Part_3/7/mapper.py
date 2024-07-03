#!/usr/bin/env python
import sys

for line in sys.stdin:
    data = line.strip().split('"')
    # if it has 3 parts atleast (has 9 including spaces)
    if len(data) > 2:
        # split to get status and size
        status_part = data[2].strip().split(' ')
        if len(status_part) > 1:
          status = status_part[0].strip()
          if status == "404":
            print("404\t"+str(1))