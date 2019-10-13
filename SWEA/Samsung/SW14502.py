import copy

def spread(x, y):
    res = 1
    cache[x][y] = 2
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if cache[nx][ny] == 0:
            res += spread(nx, ny)


    return res


def solve(start, count):
    global cache, VIRUS, v

    if count == 3:
        ret = 0
        cache = copy.deepcopy(MAP)
        for i, j in VIRUS:
            ret += spread(i, j)
        v = min(v, ret)
        return


    for i in range(start, N*M):
        x = int(i/M)
        y = i%M

        if MAP[x][y] == 0:
            MAP[x][y] = 1
            solve(i+1, count+1)
            MAP[x][y] = 0


N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

VIRUS = []
v = 100
wall = 3


for i in range(N):
    for j in range(M):
        if MAP[i][j] == 1:
            wall += 1
        if MAP[i][j] == 2:
            VIRUS.append((i,j))

solve(0, 0)
print(N*M - wall - v)

