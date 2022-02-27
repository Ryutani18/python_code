import math

jikkan = {
    0: "癸",
    1: "甲",
    2: "乙",
    3: "丙",
    4: "丁",
    5: "戊",
    6: "己",
    7: "庚",
    8: "辛",
    9: "壬",
}

zodiac = {
    0: "亥",
    1: "子",
    2: "丑",
    3: "寅",
    4: "卯",
    5: "辰",
    6: "巳",
    7: "午",
    8: "未",
    9: "申",
    10: "酉",
    11: "戌",
}

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

day = {
    0 : "土",
    1 : "日",
    2 : "月",
    3 : "火",
    4 : "水",
    5 : "木",
    6 : "金",
}

ichiryuu = {
    1 : [1,4],
    2 : [2,7],
    3 : [3,10],
    4 : [1,4],
    5 : [4,5],
    6 : [6,7],
    7 : [7,10],
    8 : [1,8],
    9 : [4,9],
    10 : [7,10],
    11 : [10,11],
    12 : [0,1],
}

fujouju = {
    0 : [6,14,22,30],
    1 : [3,11,19,27],
    2 : [2,10,18,26],
    3 : [1,9,17,25],
    4 : [4,12,20,28],
    5 : [5,13,21,29],
}

kamiyoshinichi = [0,24,6,7,9,10,14,16,19,21,22,25,28,31,33,34,36,37,38,40,42,43,44,45,46,48,49,52,55,56,57,58]

daimyonichi = [6,7,8,9,10,14,16,19,21,24,29,32,39,41,42,43,44,46,47,48,53,55,56,57,58]

ten_on_nichi = []

rokuyou = ["大安","赤口","先勝","友引","先負","仏滅"]

def calculate(y,m,d):
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
    DM = d
    for i in range(1,m):
        DM += month[i]
    DY = (y-1) * 365 + ((y-1) // 4) + DM

    K = math.ceil((DY-25.73)%29.530589)
    M = m-2 if K > d else m-1
    Y = y
    if M <= 0:
        Y -= 1
    M %= 12
    if M == 0:
        M = 12

    if DY%29.530589 >= 11 and DY%29.530589 < 12:
        print(f"〈満月〉")
    elif DY%29.530589 >= 18.15 and DY%29.530589 < 19.15:
        print(f"〈下弦の月〉")
    elif DY%29.530589 >= 25.73 and DY%29.530589 < 26.73:
        print(f"〈新月〉")
    elif DY%29.530589 >= 3.3 and DY%29.530589 < 4.3:
        print(f"〈上弦の月〉")
    
    print(f"{y}年{m}月{d}日({day[DY%7]}曜日)")
    print(f"【旧暦{Y}年{M}月{K}日】")
    print(zodiac[(y-3)%12] + "年")
    print(jikkan[DY%10] + zodiac[DY%12]  + "の日")

    if DY%60 == 1:
        print("★大吉日★")
        if DM <= 35 or DM > 311:
            print("天赦日")
    elif DY%60 == 6:
        print("★大吉日★")
    elif DY%12 == 6:
        print("★吉日★")
    elif DY%60 == 15:
        if DM > 35 and DM <= 125:
            print("★大吉日★")
            print("天赦日")
        else:
            print("★吉日★")
    elif DY%12 == 3:
        print("★吉日★")
    elif DY%60 == 31:
        if DM > 125 and DM <= 219:
            print("★大吉日★")
            print("天赦日")
    elif DY%60 == 45:
        if DM > 219 and DM <= 311:
            print("★大吉日★")
            print("天赦日")
    if DY%12 in ichiryuu[m]:
        print("一粒万倍日")

    if DY%60 in kamiyoshinichi:
        print("神吉日")
    if DY%60 in daimyonichi:
        print("大明日")

    if K in fujouju[M%6]:
        print("※不成就日※")

    print(rokuyou[(K+M)%6])

y = int(input("年を入力してください>>"))
m = int(input("月を入力してください>>"))
d = int(input("日を入力してください>>"))

calculate(y,m,d)
