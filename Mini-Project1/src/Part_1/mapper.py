#!/usr/bin/env python

import sys
import re

for line in sys.stdin:
    line = line.strip().lower()  # Convert to lowercase
    words = line.split()
    for word in words:
        word = ''.join([c for c in word if c.isalpha()])
        if word:
            print('{}\t{}'.format(word,1))
