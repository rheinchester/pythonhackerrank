def aVeryBigSum(ar):
    bigSum = 0
    for x in range(len(ar)):
        bigSum += ar[x]
    return bigSum
ar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
print(aVeryBigSum(ar))
