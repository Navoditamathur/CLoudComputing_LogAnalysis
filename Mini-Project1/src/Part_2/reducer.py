#!/usr/bin/env python

import sys

def main():
    current_ngram = None
    ngram_count = 0

    for line in sys.stdin:
        ngram, count = line.strip().split("\t")

        if current_ngram == ngram:
            ngram_count += int(count)
        else:
            if current_ngram:
                print("{}\t{}".format(current_ngram, ngram_count))
            current_ngram = ngram
            ngram_count = int(count)

    if current_ngram:
        print("{}\t{}".format(current_ngram, ngram_count))

if __name__ == "__main__":
    main()
