#!/usr/bin/env python

import sys

total_post_requests = 0

for line in sys.stdin:
    key, value = line.strip().split("\t")
    if key == "POST":
        total_post_requests += int(value)

print("Total POST requests:", total_post_requests)
