#!/usr/bin/env python

import sys
import re

total_data_requested = 0

for line in sys.stdin:
    key, value = line.strip().split("\t")
    if key == "size":
        # If the size is not "-"
        if not bool(re.match('^\d+$', value)):
            value = 0
        total_data_requested += int(value)

print("Total data requested on 19/Dec/2020 (in bytes):", total_data_requested)
