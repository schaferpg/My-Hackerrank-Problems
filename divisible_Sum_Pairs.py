#https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

def divisibleSumPairs(n, k, ar):
    x = 0
    counter = 0
    while x < n:
        y = x+1
        while x < y & y < n:
            sum = ar[x] + ar[y]
            if sum % k == 0:
                counter += 1  
            y += 1
        x += 1            
    return counter
