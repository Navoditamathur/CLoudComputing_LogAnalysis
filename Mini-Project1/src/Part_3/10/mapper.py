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
                date = date_part.strip('[')
                # get status and size
                status_part = data[2].strip().split(' ')
                if len(status_part) > 1:
                    status = status_part[0].strip()
                    size = status_part[1].strip()
                    if "16/Jan/2022" in date and status == "200":
                        print("size\t" + size)