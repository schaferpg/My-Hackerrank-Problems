#!/bin/python3
# https://www.hackerrank.com/challenges/picking-numbers/problem
import sys

def pickingNumbers(a):
    x = 0
    large = 0
    
    # Solved this by counting the total number of times a number appears in the array added to the total number of times the number 
    # that is one above it. Example: 1 and 2, in sample input 0, 1 appears once while 2 appears zero times so count = 1. Using one more 
    # example 3 and 4: 3 appears two times in the sample input 0 and 4 appears once. So count = 3 and I used an if statement to 
    # ensure I got the largest count each time it ran through the loop.
    
    while x <= max(a):
        count = 0
        for i in range(2):
            for ar in a:
                if (x+i) == ar:
                    count += 1
        if count > large:
            large = count
        x += 1    
    return large
            
         

if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = pickingNumbers(a)
    print(result)
