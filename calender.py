year = {
    0 : [1,7,18,24],
    1 : [2,8,13,19],
    2 : [3,14,20,25],
    3 : [4,9,15,26],
    4 : [10,16,21,27],
    5 : [0,5,11,22],
    6 : [6,12,17,23],
}

day = {
    0 : "日",
    1 : "月",
    2 : "火",
    3 : "水",
    4 : "木",
    5 : "金",
    6 : "土",
}

month = {
    1 : 0,
    2 : 3,
    3 : 3,
    4 : 6,
    5 : 1,
    6 : 4,
    7 : 6,
    8 : 2,
    9 : 5,
    10 : 0,
    11 : 3,
    12 : 5,
}

def calculator(y,m,d):

    if y == 0:
        return
    elif y < 0:
        y += 1

    for k,v in year.items():
        if y%28 in v:
            val = k
    val += month[m] + (d-1)

    if y <= 0:
        y -= 1

    if y%4 == 0 and m > 2:
        val += 1

    print(f"{y}年{m}月{d}日は{day[val%7]}曜日です。")

y = int(input("年を入力してください>>"))
m = int(input("月を入力してください>>"))
d = int(input("日を入力してください>>"))

calculator(y,m,d)