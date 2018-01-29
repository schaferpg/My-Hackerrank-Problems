# https://www.hackerrank.com/challenges/bon-appetit/problem

def bonAppetit(n, k, b, ar):
    total = 0
    for i in range(len(ar)):
        total += ar[i]
    price = total - ar[k]
    if (price//2) == b:
        return "Bon Appetit"
    else:
        overcharge = (ar[k]//2)
        return overcharge
