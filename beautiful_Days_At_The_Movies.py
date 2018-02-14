# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem


def find_Reverse(num):
    num_Array = [i for i in str(num)]
    rev_Array = []
    x = 0
    large = len(num_Array) - 1
    while x <=  large:
        # reverses the num_Array by appending the last value first 
        # and then I later join it so I have a complete num when returning it.
        rev_Array.append(num_Array[large])
        large -= 1
    return int("".join(rev_Array))
        
def beautiful_Days(i, j, k):
    num_Array = []
    while i <= j:
        #creates an array from i to j
        num_Array.append(i)
        i+=1
    total = 0
    for n in num_Array:
        value = n - find_Reverse(n)
        if value % k == 0:
            total += 1
    return total
if __name__ == "__main__":
    i, j, k = input().strip().split(' ')
    i, j, k = [int(i), int(j), int(k)]
    result = beautiful_Days(i, j, k)
    print(result)
