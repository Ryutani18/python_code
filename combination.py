def permulation(n,m):
    if m == 1:
        return n
    return n * permulation(n-1,m-1)

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

def combination(n,m):
    return permulation(n,m) / factorial(m)

print(combination(60,30))