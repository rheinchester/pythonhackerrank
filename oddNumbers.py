def  oddNumbers(l, r):
    arr = []
    if l < r:
        for x in range(l,r+1):
            if x % 2 != 0:
                arr.append(x)
        return arr
            
        
l = 2
r = 5
print(oddNumbers(l, r))

        
