# https://www.hackerrank.com/challenges/halloween-sale/problem
import sys

def howManyGames(p, d, m, s):
    total = counter = 0
    price = p
    while total <= s:
        total += price
        if total >= s:
            break
        price -= d
        if price <= m:
            price = m
        counter += 1
    return counter

if __name__ == "__main__":
    p, d, m, s = input().strip().split(' ')
    p, d, m, s = [int(p), int(d), int(m), int(s)]
    answer = howManyGames(p, d, m, s)
    print(answer)
