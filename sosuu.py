a = int(input("数値を入力してください>>"))
array = list()
sosuu = list()
bool = True
i = 1
while i < a:
    for s in sosuu:
        if i % s == 0:
            bool = False
            break
    if bool == True:
        if a % i == 0:
            array.append(i)
        else:
            sosuu.append(i)
    else:
        bool = True
    i += 1

array.append(a)
for arr in array:
    print(arr)

print(sosuu)