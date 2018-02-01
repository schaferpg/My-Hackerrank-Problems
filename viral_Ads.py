#!/bin/python3
# https://www.hackerrank.com/challenges/strange-advertising/problem
import sys

def viral_Ads(n):
    shared = 5
    total = 0
    for i in range(n):
        total += shared // 2
        shared = (shared//2) * 3
    return total

if __name__ == "__main__":
    n = int(input().strip())
    result = viral_Ads(n)
    print(result)
