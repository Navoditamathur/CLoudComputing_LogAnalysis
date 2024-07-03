#!/usr/bin/env python

import sys

# Initialize an empty dictionary to ip counts
ip_counts = {}

# Iterate over input lines from stdin
for line in sys.stdin:
    # Split the input line into path and count fields
    ip, count = line.strip().split("\t")
    
    # Update the count for the current path in the dictionary
    ip_counts[ip] = ip_counts.get(ip, 0) + int(count)

# Find the path with the maximum count
max_ip = max(ip_counts, key=ip_counts.get)
max_access = ip_counts[max_ip]

# Print the IP with the most access from and its count
print("IP with most accesses from:", max_ip)
print("Number of time accessed:", max_access)
