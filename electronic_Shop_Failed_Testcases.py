#!/bin/python3
# https://www.hackerrank.com/challenges/electronics-shop/problem

import sys

def getMoneySpent(keyboards, drives, s):
    spent = 0
    for key in keyboards:
        for usb in drives:
            # No need to initialize cost up top.  Put variables as close as
            # possible to where you use them
            cost = key + usb
            # The bug was using < instead of <=
            if cost <= s:
                # Usually, it's clear to use max when updating a max value.
                spent = max(spent, cost)
    # Python has an inline if syntax that's good for cases like this:
    return spent if spent > 0 else -1

s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
