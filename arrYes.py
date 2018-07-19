# Complete the function below.

def  findNumber(arr, k):
    for item in arr:
        answer = 'No'
        if k in arr:
            answer = 'Yes'
    return answer
arr = [5,6,3,2,23,3]
k = 1
print(findNumber(arr, k))
