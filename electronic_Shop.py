#!/bin/python3
# https://www.hackerrank.com/challenges/electronics-shop/problem

import sys

def get_Money_Spent(key, usb, s):
    cost = total = 0
    for k in key:
        for u in usb:
            total = k + u
            if total > cost and total <= s:
                cost = total
    if cost > 0:
        return cost
    else:
        return "-1"

s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
