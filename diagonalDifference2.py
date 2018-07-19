def diagonalDifference(arr):
    minus = -1
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            primeDiag = arr[x][y]
            secDiag = arr[-1][0]
            primeDiag = primeDiag + arr[x+1][y+1]
            secDiag = secDiag + arr[minus-1][y+1]
            diff = abs(primeDiag - secDiag)
            print(diff)
arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
#arr = [[-1, 1, -7, -8],[-10, -8, -5, -2],[0, 9, 7, -1],[4, 4, -2, 1]]
print(diagonalDifference(arr))

