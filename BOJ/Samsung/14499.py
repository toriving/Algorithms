N, M, y, x, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
move = list(map(int, input().split()))


dy, dx = [0, 0, -1, 1], [1, -1, 0, 0]
dice = [0] * 6
dcur = 0
for m in move:
    m -= 1

    nx = x + dx[m]
    ny = y + dy[m]

    if nx < 0 or ny < 0 or nx > M-1 or ny > N-1:
        nx = x
        ny = y
        continue
    else:
        x = nx
        y = ny

    tmp = dice.copy()

    if m == 0:
        tmp[1] = dice[2]
        tmp[2] = dice[3]
        tmp[3] = dice[5]
        tmp[5] = dice[1]
    elif m == 1:
        tmp[1] = dice[5]
        tmp[2] = dice[1]
        tmp[3] = dice[2]
        tmp[5] = dice[3]
    elif m == 2:
        tmp[0] = dice[5]
        tmp[2] = dice[0]
        tmp[4] = dice[2]
        tmp[5] = dice[4]
    else:
        tmp[0] = dice[2]
        tmp[2] = dice[4]
        tmp[4] = dice[5]
        tmp[5] = dice[0]

    dice = tmp

    if MAP[y][x] == 0:
        MAP[y][x] = dice[2]
    else:
        dice[2] = MAP[y][x]
        MAP[y][x] = 0


    print(dice[5])
