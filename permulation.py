def permulation(n,m):
    if m == 1:
        return n
    return n * permulation(n-1,m-1)

permulation()