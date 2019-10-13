def spread():
    cache = [[0] * C for _ in range(R)]
    for y in range(R):
        for x in range(C):
            if MAP[y][x] >= 5:
                dust = MAP[y][x] // 5
                for dx, dy in (-1,0), (1,0), (0,1), (0,-1):
                    ny, nx = y+dx, x+dy
                    if 0 <= ny < R and 0 <= nx < C and MAP[ny][nx] != -1:
                        cache[ny][nx] += dust
                        MAP[y][x] -= dust

    for y in range(R):
        for x in range(C):
            MAP[y][x] += cache[y][x]

def cleaner():
    for i in range(py[0]-2, -1, -1):
        MAP[i+1][0] = MAP[i][0]
    for i in range(C-1):
        MAP[0][i] = MAP[0][i+1]
    for i in range(py[0]):
        MAP[i][C-1] = MAP[i+1][C-1]
    for i in range(C-2, -1, -1):
        MAP[py[0]][i+1] = MAP[py[0]][i]

    MAP[py[0]][1] = 0

    for i in range(py[1]+1, R-1):
        MAP[i][0] = MAP[i+1][0]
    for i in range(C-1):
        MAP[R-1][i] = MAP[R-1][i+1]
    for i in range(R-2, py[1]-1, -1):
        MAP[i+1][C-1] = MAP[i][C-1]
    for i in range(C-2, -1, -1):
        MAP[py[1]][i+1] = MAP[py[1]][i]

    MAP[py[1]][1] = 0


R, C, T = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(R)]
py = []

for y in range(R):
    if MAP[y][0] == -1:
        py.append(y)
        py.append(y+1)
        break

for _ in range(T):
    spread()
    cleaner()

print(sum(map(sum, MAP))+2)