#!/usr/bin/env python

def fizzbuzz(n):
    for i in range(n):
        if i % 15 == 0:
            print "fizzbuzz"
        elif i % 3 == 0:
            print "fizz"
        elif i % 5 == 0:
            print "buzz"
        else:
            print i

#what the fuck is python.