def mul(arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0] * mul(arr[1:])

def lcm(arr):
    n = len(arr)
    return mul(arr) / gcd(arr) ** (n-1)

def gcd(arr):
    n = len(arr)
    if n == 2:
        if arr[0] == 0 or arr[1] == 0:
            return arr[0] + arr[1]
        if arr[0]>arr[1]:
            arr[0] = arr[0]%arr[1]
        else:
            arr[1] = arr[1]%arr[0]
        return gcd(arr)
    for i in range(n-1):
        arr[i] = gcd(arr[i:i+2])
    arr.pop(-1)
    return gcd(arr)

print(lcm([2,3,5]))