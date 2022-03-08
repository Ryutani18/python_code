import math

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
  num = float(input("値を入力>>"))
  print(compile(num))

def compile(num):
  d,h = divmod(num,86400)
  h,min = divmod(h,3600)
  # min,h = math.modf(h/3600)
  min,sec = divmod(min,60)
  # sec,min = math.modf(min*60)
  # sec *= 60
  y,d = divmod(d+1,365.25)
  d = -(-d//1)
  y += 1
  if y%4 == 0:
    month[2] += 1
  m = 1
  while d > month[m]:
    d -= month[m]
    m += 1
  return f'{y:02.0f}年{m:02.0f}月{d:02.0f}日{h:02.0f}時{min:02.0f}分{sec:02.0f}秒'
  # return '%d年%d月%d日%02d時%02d分%02d秒' % (int(y),int(m),int(d),int(h),int(min),int(sec))

if __name__ == "__main__":
  main()