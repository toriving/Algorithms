n, m = map(int,input().split())
board = [list(*input().split()) for _ in range(n)]
ret = 987654321
dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
for y in range(n):
    for x in range(m):
        if board[y][x] == 'B':
            blue = (y,x)
        elif board[y][x] == 'R':
            red = (y,x)

def check(y, x):
    return 0 <= x < m and 0 <= y < n and board[y][x] != '#'


def move(y, x, dy, dx):
    # 상하좌우
    # while board[y + dy][x + dx] != '#':
    while board[y+dy][x+dx] != '#' and board[y][x] != 'O':
        y += dy
        x += dx

    return y, x

def dfs(ry, rx, by, bx, cnt):
    global ret
    if cnt == 10:
        ret = min(ret, 987654321)
        return

    if board[ry][rx] == 'O':
        ret = min(cnt, ret)
        return

    for i in range(4):
        rny, rnx = move(ry, rx, dy[i], dx[i])
        bny, bnx = move(by, bx, dy[i], dx[i])

        if not check(rny, rnx):
            rny = ry
            rnx = rx

        if not check(bny, bnx):
            bny = by
            bnx = bx

        if board[bny][bnx] == 'O':
            continue

        if rny == bny and rnx == bnx:
            if i == 0:
                if ry > by:
                    rny += 1
                else:
                    bny += 1
            elif i == 1:
                if ry > by:
                    bny -= 1
                else:
                    rny -= 1
            elif i == 2:
                if rx > bx:
                    rnx += 1
                else:
                    bnx += 1
            else:
                if rx > bx:
                    bnx -=1
                else:
                    rnx -=1



        cnt += 1
        dfs(rny, rnx, bny, bnx, cnt)
        cnt -= 1


dfs(*red,*blue, 0)
print(ret if ret != 987654321 else -1)