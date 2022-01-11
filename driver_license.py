#自動車免許

print("自動車免許試験正誤問題")

title = input("タイトル：")
page = int(input("ページ数："))
num = list(map(int, input("問題数：").split(',')))
if len(num) == 1:
  num.insert(0,1)
array = list()

for i in range(num[0], num[1]+1):
  array.append(f"第{i}問." + input(f"{i}問. "))

print("答え合わせ")
count = 0
for i in array:
  a = input(f"{i}")
  if a == "y":
    count += 1

print(title)
print(f"正答率:{count * 100 / (num[1]-num[0]+1)}%")