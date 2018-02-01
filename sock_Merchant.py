#!/bin/python3
# https://www.hackerrank.com/challenges/sock-merchant/problem
import sys

def sock_Merchant(n, ar):
    check = []
    test = []
    total = 0
    # This for loop finds the unique numbers in ar
    for a in ar:
        if a not in check:
            check.append(a)
    ####
    
    #This part counts that amount of times that a unique number appears
    #In an array then adds it to a variable total
    for c in check:
        counter = 0
        for a in ar:
            if c == a:
                counter += 1
        total += counter//2
    return total

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)
