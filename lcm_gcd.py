def lcm(n,m):
    return n*m/gcd(n,m)

def gcd(n,m):
    if n == 0 or m == 0:
        return n+m
    if n>m:
        n = n%m
    else:
        m = m%n
    return gcd(n,m)

def gcd_arr(arr):
    n = len(arr)
    if n == 2:
        return gcd(arr[0],arr[1])
    for i in range(n-1):
        arr[i] = gcd(arr[i],arr[i+1])
    arr.pop(-1)
    return gcd_arr(arr)

def lcm_arr(arr):
    n = len(arr)-1
    return mul(arr) / gcd_arr(arr) ** n

def mul(arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0] * mul(arr[1:])

print(gcd([2,3,5,7]))