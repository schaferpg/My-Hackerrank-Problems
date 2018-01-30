#!/bin/python3

# https://www.hackerrank.com/challenges/save-the-prisoner/problem

import sys

def saveThePrisoner(n, m, s):
    change = (m+s-1)%n
    if change == 0:
        return n
    else:
        return change

    
    
t = int(input().strip())
for a0 in range(t):
    n, m, s = input().strip().split(' ')
    n, m, s = [int(n), int(m), int(s)]
    result = saveThePrisoner(n, m, s)
    print(result)
