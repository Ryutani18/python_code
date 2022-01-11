import math

a = int(input("数値を入力してください>>"))

def add_num(a):
    n = 0
    while a > 0:
        n += a % 10
        a = math.floor(a / 10)
    return n

print(add_num(a))

while a > 10:
    a = add_num(a)

print(a)