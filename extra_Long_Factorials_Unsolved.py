# https://www.hackerrank.com/challenges/extra-long-factorials/forum

import sys

def extra_Long_Factorials(n):
    counter = total = 1
    while n >= counter:
        total = total * counter
        counter += 1
    return total

if __name__ == "__main__":
    n = int(input().strip())
    extraLongFactorials(n)
