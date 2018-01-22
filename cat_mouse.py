#!/bin/python3
# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

import sys

def catAndMouse(x, y, z):
    a_Mouse = abs(x - z)
    b_Mouse = abs(y - z)
    if a_Mouse == b_Mouse:
        return "Mouse C"
    elif a_Mouse < b_Mouse:
        return "Cat A"
    else:
        return "Cat B"
    
if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        x, y, z = input().strip().split(' ')
        x, y, z = [int(x), int(y), int(z)]
        result = catAndMouse(x, y, z)
        print (result)


