#!/usr/bin/env python
import sys

for line in sys.stdin:
    # Split the line on "" to get the data
    data = line.strip().split('"')
    # if it has 3 parts atleast
    if len(data) > 2:
        # split the data to get ip, date time stamp and 2 other fields
        request = data[0].strip().split(' ')
        # if it has 4 fields
        if len(request) > 3:
            # get the date
            date_part = request[3].strip()
            if date_part:
                # strip '[']
                date = date_part.strip('[')
                # If it is in date part
                if "19/Dec/2020" in date:
                    # split the 2nd part to get status & size
                    size_part = data[2].strip().split(' ')
                    if len(size_part) > 1:
                        size = size_part[1].strip()
                        print("size\t" + size)
