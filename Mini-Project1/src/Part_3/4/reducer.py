#!/usr/bin/env python

import sys

# Initialize an empty dictionary to store path counts
path_counts = {}

# Iterate over input lines from stdin
for line in sys.stdin:
    # Split the input line into path and count fields
    path, count = line.strip().split("\t")
    
    # Update the count for the current path in the dictionary
    path_counts[path] = path_counts.get(path, 0) + int(count)

# Find the path with the maximum count
max_path = max(path_counts, key=path_counts.get)
max_hits = path_counts[max_path]

# Print the path with the maximum hits and its count
print("Path with most hits:", max_path)
print("Number of hits:", max_hits)