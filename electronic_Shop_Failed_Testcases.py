#!/bin/python3
# https://www.hackerrank.com/challenges/electronics-shop/problem

import sys

def getMoneySpent(keyboards, drives, s):
    cost = 0
    spent = 0
    for key in keyboards:
        for usb in drives:
            cost = key + usb
            if cost > spent and cost < s:
                spent = cost
    if spent > 0:
        return spent
    else:
        return -1

s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
