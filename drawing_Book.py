#!/bin/python3
# https://www.hackerrank.com/challenges/drawing-book/problem

def solve(n, p):
    start = p//2
    end = (n-p)//2
    if (n-p) == 1 and n%2 == 0 and p > 1:
        return 1
    if start < end:
        return start
    else:
        return end
    

n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)
