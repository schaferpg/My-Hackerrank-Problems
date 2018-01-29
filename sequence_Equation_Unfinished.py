#!/bin/python3
# https://www.hackerrank.com/challenges/permutation-equation/problem
import sys

def permutationEquation(p):
    for a in p:
        print(a)

if __name__ == "__main__":
    n = int(input().strip())
    p = list(map(int, input().strip().split(' ')))
    result = permutationEquation(p)
    print ("\n".join(map(str, result)))
