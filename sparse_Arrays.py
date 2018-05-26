# https://www.hackerrank.com/challenges/sparse-arrays/problem

def matchingStrings(strings, queries):
    count_Arr = []
    for q in queries:
        count = 0
        for s in strings:
            if q == s:
                count += 1
        count_Arr.append(count)
    return count_Arr
strings_count = int(input())
strings = []
for _ in range(strings_count):
    strings_item = input()
    strings.append(strings_item)

queries_count = int(input())
queries = []
for _ in range(queries_count):
    queries_item = input()
    queries.append(queries_item)

answer = matchingStrings(strings, queries)
for a in answer:
    print(a)
