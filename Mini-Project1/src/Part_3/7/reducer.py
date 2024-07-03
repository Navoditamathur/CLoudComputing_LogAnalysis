#!/usr/bin/env python

import sys

total_404_requests = 0

for line in sys.stdin:
    key, value = line.strip().split("\t")
    if key == "404":
        total_404_requests += int(value)

print("Total requests with 404 status code:", total_404_requests)
