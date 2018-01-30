#!/bin/python3

# https://www.hackerrank.com/challenges/save-the-prisoner/problem

import sys

def save_The_Prisoner(n, m, s):
    # This allows me to find the prisoners Id number
    prison_Id = m + s - 1
    #
    nums = []
    # Make's a list the prisoner's Ids
    for i in range(n):
        i += 1
        nums.append(i)
    # Not sure what logic I can use in this case but the while loop seems kinda ugly.
    # I'm trying to make sure it the program subtracts the number of prisoners 
    # from the prison_Id until there's a match to a prisoner's id.
    x = 2
    while True:
        if prison_Id not in nums:
            prison_Id -= n
        else:
            False
            return prison_Id

    
    
t = int(input().strip())
for a0 in range(t):
    n, m, s = input().strip().split(' ')
    n, m, s = [int(n), int(m), int(s)]
    result = saveThePrisoner(n, m, s)
    print(result)
