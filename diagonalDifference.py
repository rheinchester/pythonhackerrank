def diagonalDifference(arr):
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            primDiag = arr[0][0] + arr[1][1] + arr[2][2]
            secDiag = arr[-1][0] + arr[-2][1] + arr[-3][2]
            diff = abs(primDiag - secDiag)
        return diff
arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
print(diagonalDifference(arr))
