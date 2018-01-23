#!/bin/python3
# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

import sys

def cat_and_mouse(x, y, z):
    a_mouse = abs(x - z)
    b_mouse = abs(y - z)
    if a_mouse == b_mouse:
        return "Mouse C"
    elif a_mouse < b_mouse:
        return "Cat A"
    else:
        return "Cat B"
    
if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        x, y, z = input().strip().split(' ')
        x, y, z = [int(x), int(y), int(z)]
        result = cat_and_mouse(x, y, z)
        print(result)


