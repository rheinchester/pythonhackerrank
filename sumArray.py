
# Complete the simpleArraySum function below.
#
def solve(a, b):
    pointA = 0
    pointB = 0
    for x in range(len(a)):
        if a[x] > b[x]:
            pointA += 1
        elif a[x] == b[x]:
            pass
        else:
            pointB += 1
    arrPoints = [pointA, pointB]
    return arrPoints
a = [5,9,7]
b = [9,9,13]
print(solve(a, b))
