# https://www.hackerrank.com/challenges/halloween-sale/problem
import sys

def how_Many_Games(p, d, m, s):
    total = counter = 0
    price = p
    # This while loop makes sure that the total being spent does not exceed the money you have.
    while total <= s:
        total += price
        # This double checks what the while loop does.
        if total >= s:
            break
        price -= d
        # This makes sure that the price doesn't go below what the store has set as the price floor.
        if price <= m:
            price = m
        counter += 1
    return counter

if __name__ == "__main__":
    p, d, m, s = input().strip().split(' ')
    p, d, m, s = [int(p), int(d), int(m), int(s)]
    answer = how_Many_Games(p, d, m, s)
    print(answer)
