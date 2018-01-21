#!/usr/bin/env python

def fizzbuzz(n):
    for i in range(n):
        if i % 30 == 0:
            print "fizzbuzzboom"
        elif i % 15 == 0:
            print "fizzbuzz"
        elif i % 3 == 0:
            print "fizz"
        elif i % 10 == 0:
            print "buzzboom"
        elif i % 6 == 0:
            print "fizzboom"
        elif i % 5 == 0:
            print "buzz"
        elif i % 2 == 0:
            print "boom"
        else:
            print i
