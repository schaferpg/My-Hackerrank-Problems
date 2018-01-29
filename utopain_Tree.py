#!/bin/python3

# https://www.hackerrank.com/challenges/utopian-tree/problem

import sys

def utopianTree(n,t):
    for i in range(t):
        height = 1
        if n > 0:
            height = 2
        else:
            return 1
    for j in range(n-1):
        if j%2 == 0:
            height +=1
        else:
            height *= 2
    return height

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        result = utopianTree(n,t)
        print(result)
