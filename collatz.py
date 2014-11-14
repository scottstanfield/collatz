#!/usr/bin/env python -t
import sys
from decimal import *

def collatz(x):
    seq = [x]

    while x > 1:
        if x % 2 == 0:
            x = x / 2
        else:
            x = 3*x + 1
        seq.append(x)

    return seq

try:
    start = int(Decimal(sys.argv[1]))
except:
    print "How to run: collatz starting-number (default is 10)"
    start = 10

seq = collatz(start)
print seq
print "collatz(%d) has %d items" % (start, len(seq))

