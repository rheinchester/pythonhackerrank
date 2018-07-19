def diagonalDifference(arr):
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            print(x,'--------',arr[y+1])
            
    
arr = [[-1, 1, -7, -8],[-10, -8, -5, -2],[0, 9, 7, -1],[4, 4, -2, 1]]
print(diagonalDifference(arr))
