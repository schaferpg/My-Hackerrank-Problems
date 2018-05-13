# https://www.hackerrank.com/challenges/arrays-ds/problem
#!/bin/python3

import os
import sys

def reverseArray(a):
    rev_A = []
    for i in range(len(a)):
        rev_A.append(a[-1-i])
    return rev_A
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
