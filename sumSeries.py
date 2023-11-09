

def summingSeries(n):
    # Write your code here
    sum = 0
    while(n > 0):
        sum += 2 * n - 1
        n-= 1
    return sum


res = summingSeries(3)
print(res)
        
        
