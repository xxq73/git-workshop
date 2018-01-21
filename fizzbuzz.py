#!/usr/bin/env python

def fizzbuzz(n):
    for i in range(1, n + 1):
        s = ""
        if i % 3 == 0:
            s += "fizz"
        if i % 5 == 0:
            s += "buzz"
        if i % 7 == 0:
            s += "bizz"
        if not s:
            s = "%d" % i
        print s
