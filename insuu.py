insuu = list()
num = int(input("数値を入力してください>>"))
for i in range(1,num+1):
    if num % i == 0:
        insuu.append(i)
for i in insuu:
    print(i)