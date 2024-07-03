#!/usr/bin/env python

import sys

current_word = None
current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t',1)

    if current_word == word:
        current_count += int(count)
    else:
        if current_word:
            print('{}\t{}'.format(current_word,current_count))
        current_word = word
        current_count = int(count)

if current_word == word:
    print('{}\t{}'.format(current_word,current_count))
