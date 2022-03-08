import re

month = {
  1 : 31,
  2 : 28,
  3 : 31,
  4 : 30,
  5 : 31,
  6 : 30,
  7 : 31,
  8 : 31,
  9 : 30,
  10 : 31,
  11 : 30,
  12 : 31,
}

def main():
  t = input("年月日を入力>>")
  t = re.split('[/:]',t)
  t = list(map(int,t))
  print(t)

  if t[3] < 0 or t[3] >= 24:
    print("invalid")
    return
  if t[4] < 0 or t[4] >= 60:
    print("invalid")
    return
  if t[5] < 0 or t[5] >= 60:
    print("invalid")
    return

  val = t[3] * 3600 + t[4] * 60 + t[5]

  print(calculate(t[0],t[1],t[2],val))

def calculate(y,m,d,val):
  if y <= 0:
    return
  if m < 1 or m > 12:
    print("invalid")
    return
  if y%4 == 0:
    month[2] += 1
  if d > month[m]:
    print("invalid")
    return
  DM = d-1
  for i in range(1,m):
    DM += month[i]
  DY = (y-1) * 365 + ((y-1) // 4) + DM
  VAL = DY * 86400 + val
  return VAL

if __name__ == "__main__":
  main()