# Add URL for hacker rank problem:
# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

# Python uses "snake-case" (using underscores) for function names.
# I'm not sure why hacker rank uses the wrong style.
def divisible_sum_pairs(n, k, ar):
    x = 0
    counter = 0
    # A while loop with x += 1 is the same a for loop.
    # Prefer for-loops because you don't have to update the loop variable.
    while x < n:
        y = x+1
        # X is always < y, since you defined y = x + 1
        while x < y & y < n:
            # Don't use sum in python, it's an already defined function name.
            # It'll work most of the time but can result in strange errors.
            # Total is a better name.
            sum = ar[x] + ar[y]
            if sum % k == 0:
                counter += 1  
            y += 1
        x += 1            
    return counter

def divisible_sum_pairs2(n, k, ar):
    counter = 0
    # n == len(ar), but using len makes it clear we want to index `ar`.

    # i, j, and k are the most common index variables.  x, y, z usually
    # represent an actual element in the array, like ar[i]
    for i in range(len(ar)):
        for j in range(i + 1, len(ar)):
            total = ar[i] + ar[j]
            if total % k == 0:
                counter += 1

    return counter
            
