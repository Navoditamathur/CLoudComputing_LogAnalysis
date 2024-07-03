#!/usr/bin/env python

import sys

total_hits = 0

# Count the total number of hits and print it to output
for line in sys.stdin:
    key, value = line.strip().split("\t")
    if key == "hits":
        total_hits += int(value)

print("Total hits from IP 96.32.128.5:", total_hits)