#!/bin/python3
# https://www.hackerrank.com/challenges/the-hurdle-race/problem
import sys

def hurdleRace(k, height):
    large = height[0]
    for i in range(len(height)):
        if large < height[i]:
            large = height[i]
    if (large-k) > 0:
        return large - k
    else:
        return 0
    
    
if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    height = list(map(int, input().strip().split(' ')))
    result = hurdleRace(k, height)
    print(result)
