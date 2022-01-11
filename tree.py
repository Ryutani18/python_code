H, W = map(int, input().split(' '))
data = list()
points = list()
for h in range(H):
    data.append(list(map(int, input().split(' '))))
for w in range(W):
    index = [w]
    box = list()
    h = 0
    while h < H:
        print(index)
        if h == H-1:
            if not box:
               break
            h = box[-1][0]
            index = box[-1][1]
            print(index)
            box.pop()
        for i in index:
            if len(index) > 1:
                box.append([h,index[1:]])
            if i == 0:
                sample = [-1, data[h+1][i], data[h+1][i+1]]
            elif i == W-1:
                sample = [data[h+1][i-1], data[h+1][i], -1]
            else:
                sample = [data[h+1][i-1], data[h+1][i], data[h+1][i+1]]
            # index += sample.index(max(sample)) - 1
            num = [i-1 for i, x in enumerate(sample) if x == max(sample)]
            for n in range(len(num)):
                num[n] += i
            index = num
            h += 1
            break