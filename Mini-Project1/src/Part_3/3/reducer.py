#!/usr/bin/env python

import sys

# Count the total number of method types and print it to output
methods = set()

for line in sys.stdin:
    method, _ = line.strip().split("\t")
    methods.add(method)

print("Total HTTP request methods:", len(methods))
print("HTTP request methods:", ', '.join(methods))
