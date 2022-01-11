sosuu = list()
bool = True
a = int(input("数値を入力してください>>"))
for i in range(2,a+1):
    for s in sosuu:
        if i % s == 0:
            bool = False
            break
    if bool:
        sosuu.append(i)
    else:
        bool = True

print(sosuu)

print(len(sosuu))