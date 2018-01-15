#!/bin/python3

import sys

def get_Small(b):
    # Finds the smallest number in Group B
    small = b[0]
    for br in b:
        if small > br:
            small = br
    return small

def find_Factors(a, small):
    # Finds the common factors of all the numbers for the smallest number in group b
    factors = []   
    for ar in a:
        temp = ar
        while temp <= small:
            if small%temp == 0:
                factors.append(temp)
            temp += 1
    return factors

def find_Common_Factors(fact, n):
    new_Fact = []
    # This next part is eliminating all the numbers that appear only once in the array. 
    # I do this because If they only appear once then they are only factors of one number
    # in the first array. 
    for f in fact:
        total = 0
        for j in fact:
            if f == j:
                total += 1
        if total < n:
            fact.remove(f)
    # This for statement is me elimnating all the repeating numbers that occur in array fact. 
    for f in fact:
        if f not in new_Fact:
            new_Fact.append(f)
    return new_Fact                

def get_Mult(factors, b, m):
    # I use checker because all instances have to be divisable by the number.
    # So I add 1 everytime it runs through and if checker == the len of array b 
    # Then it means every number is divisible by it. 
    sim_Nums = 0
    for f in factors:
        checker = 0
        for br in b:
            if br%f == 0: 
                checker += 1
            if checker == m:
                sim_Nums += 1
    return sim_Nums
            
n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))

factors = find_Common_Factors(find_Factors(a, get_Small(b)), n)
print(get_Mult(factors, b, m))
