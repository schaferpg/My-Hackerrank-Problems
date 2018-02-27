# https://www.hackerrank.com/challenges/halloween-sale/problem
import sys

def howManyGames(p, d, m, s):
    counter = 0
    spent = temp = 20
    while spent < s:
        if temp < m:
            temp = m
        else:
            temp -= d
        spent += temp
        counter += 1
    if spent > s:
        return counter - 1
    else:
        return counter

if __name__ == "__main__":
    p, d, m, s = input().strip().split(' ')
    p, d, m, s = [int(p), int(d), int(m), int(s)]
    answer = howManyGames(p, d, m, s)
    print(answer)
