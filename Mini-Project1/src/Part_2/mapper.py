#!/usr/bin/env python

import sys
import os 

def emit_ngrams(line, n):
    line = line.strip().lower()  # Convert to lowercase
    line = ''.join([c for c in line if c.isalpha()])  # Remove non-alphabetic characters
    words = line.split()
    for word in words:
        for i in range(len(word) - n + 1):
            yield word[i:i+n], 1

def main():
    n = int(os.environ.get('N'))
    for line in sys.stdin:
        for ngram, count in emit_ngrams(line, n):
            print("{}\t{}".format(ngram, count))

if __name__ == "__main__":
    main()

