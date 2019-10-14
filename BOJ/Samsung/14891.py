import copy
def rotation(w, dir):
    if dir == 1:
        w = w[-1:] + w[:-1]
    else:
        w = w[1:] + w[:1]

    return w

wheel = [list(map(int, input())) for _ in range(4)]
k = int(input())
rot = []
for _ in range(k):
    rot.append(list(map(int,input().split())))


for idx, dir in rot:
    idx -= 1
    tmp = copy.deepcopy(wheel)
    tmp[idx] = rotation(wheel[idx], dir)
    if idx == 0:
        if wheel[0][2] != wheel[1][6]:
            tmp[1] = rotation(wheel[1], -dir)
            if wheel[1][2] != wheel[2][6]:
                tmp[2] = rotation(wheel[2], dir)
                if wheel[2][2] != wheel[3][6]:
                    tmp[3] = rotation(wheel[3], -dir)
    elif idx == 1:
        if wheel[1][6] != wheel[0][2]:
            tmp[0] = rotation(wheel[0], -dir)
        if wheel[1][2] != wheel[2][6]:
            tmp[2] = rotation(wheel[2], -dir)
            if wheel[2][2] != wheel[3][6]:
                tmp[3] = rotation(wheel[3], dir)
    elif idx == 2:
        if wheel[2][6] != wheel[1][2]:
            tmp[1] = rotation(wheel[1], -dir)
            if wheel[1][6] != wheel[0][2]:
                tmp[0] = rotation(wheel[0], dir)
        if wheel[2][2] != wheel[3][6]:
            tmp[3] = rotation(wheel[3], -dir)

    else:
        if wheel[3][6] != wheel[2][2]:
            tmp[2] = rotation(wheel[2], -dir)
            if wheel[2][6] != wheel[1][2]:
                tmp[1] = rotation(wheel[1], dir)
                if wheel[1][6] != wheel[0][2]:
                    tmp[0] = rotation(wheel[0], -dir)
    wheel = tmp


print(wheel[0][0]*1 + wheel[1][0]*2 + wheel[2][0] * 4 + wheel[3][0] * 8)