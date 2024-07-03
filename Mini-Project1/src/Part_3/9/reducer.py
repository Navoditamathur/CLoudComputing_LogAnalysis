#!/usr/bin/env python

import sys
import re

# Initialize an empty dictionary to ip data
ip_data = {}
# Initialize an empty dictionary to ip counts
ip_counts = {}

for line in sys.stdin:
    ip, count, size = line.strip().split("\t")
    # Update the count for the current path in the dictionary
    ip_counts[ip] = ip_counts.get(ip, 0) + int(count)
    # If the size is not "-"
    if not bool(re.match('^\d+$', size)):
        size = 0
    ip_data[ip] = ip_data.get(ip, 0) + int(size)

sorted_ips = sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)
print("Top 3 IPs accessed most with total data flow size (in bytes):")
for i in range(min(3, len(sorted_ips))):
    ip = sorted_ips[i][0]
    print(ip, ":", ip_data.get(ip,0))

