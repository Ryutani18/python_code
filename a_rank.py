H, W = map(int, input().split(' '))
data = list()
none = list()
array = list()
for h in range(H):
    data.append(list(map(int, input().split(' '))))
none.append(data[0])
for h in range(1,H):
    points = list()
    for w in range(W):
        points.append(None)
    none.append(points)
for h in range(1,H):
    for w in range(W):
        if none[h-1][w] == None:
            continue
        sample = list()
        if w == 0:
            sample += [-1, data[h][w], data[h][w+1]]
        elif w == W-1:
            sample += [data[h][w-1], data[h][w], -1]
        else:
            sample += [data[h][w-1], data[h][w], data[h][w+1]]
        vector = [i-1 for i, x in enumerate(sample) if x == max(sample)]
        for v in vector:
            if none[h][w+v] == None:
                none[h][w+v] = list()
            none[h][w+v].append(none[h-1][w] + data[h][w+v])
    for w in range(W):
        if none[h][w] == None:
            continue
        none[h][w] = max(none[h][w])
for n in range(len(none[H-1])):
    if none[H-1][n] == None:
        none[H-1][n] = 0
print(none[H-1])
print(max(none[H-1]))