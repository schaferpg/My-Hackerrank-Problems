# https://www.hackerrank.com/challenges/2d-array/problem

# Final prettier Solution

def array2D(arr):
    sum_Arr = []
    for i in range(4):
        for j in range(4):
            sum_Arr.append(arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])

    return max(sum_Arr)


# What I orginally had 

"""
def array2D(arr):
    sum_Arr = []
    #Vertical compenent, keeps track of where to start in the 6x6 matrix
    for i in range(4):
        #Horizontal copenent, same purpose as vertical
        for j in range(4):
            sum_Arr.append(get_Total(i,j))
    sum_Arr.sort()
    return sum_Arr[len(sum_Arr)-1]
# Finds the hourgalss sum of wherever it starts at in the 6x6 matrix
def get_Total(vert, horiz):
    total = 0
    for i in range(3):
        if i == 0 or i == 2:
            for j in range(3):
                total += arr[vert + i][horiz + j]
        else:
            total += arr[vert + 1][horiz + 1]
    return total
"""
