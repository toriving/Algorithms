
def solve(y, x, d, cnt):
    while True:
        if cnt == 4:
            bx = x - dx[d]
            by = y - dy[d]

            if MAP[by][bx] == 1:
                return
            else:
                x, y, d, cnt = bx, by, d, 0

        if MAP[y][x] == 0:
            MAP[y][x] = 2


        nd = (d + 3) % 4

        nx = x + dx[nd]
        ny = y + dy[nd]

        if MAP[ny][nx] == 0:
            x, y, d, cnt = nx, ny, nd, 0
        else:
            x, y, d, cnt = x, y, nd, cnt +1


N, M = map(int,input().split())
r, c, d = map(int,input().split())
MAP = [list(map(int,input().split())) for _ in range(N)]
dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

solve(r,c,d,0)


print(sum(map(lambda x: x.count(2),MAP)))


