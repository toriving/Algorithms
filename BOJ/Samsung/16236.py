def bfs(y, x):
    q = [(y, x)]
    dist = [[-1] * N for _ in range(N)]
    dist[y][x] = 0
    while q:
        cy, cx = q.pop(0)
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if MAP[ny][nx] <= shark and dist[ny][nx] == -1:
                    dist[ny][nx] = dist[cy][cx] + 1
                    q.append((ny, nx))

    return dist


N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
dx, dy = (0, 0, -1, 1), (-1, 1, 0, 0)
x, y = 0, 0

for i in range(N):
    for j in range(N):
        if MAP[i][j] == 9:
            y, x = i, j
            MAP[i][j] = 0
            break


shark = 2
ret = 0
cnt = 0

while True:
    dist = bfs(y, x)
    candi = []
    for i in range(N):
        for j in range(N):
            if dist[i][j] > 0 and 0 < MAP[i][j] < shark:
                candi.append((dist[i][j], i, j))
    if not candi:
        break

    candi.sort()
    target = candi[0]
    ret += dist[target[1]][target[2]]
    y, x = target[1], target[2]
    MAP[target[1]][target[2]] = 0
    cnt += 1
    if cnt == shark:
        cnt = 0
        shark += 1

print(ret)



