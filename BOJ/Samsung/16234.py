# python3 시간초과


from collections import deque

N, L, R = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(N)]
ret = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


while True:
    cache = set()
    flag = False
    change = []

    for j in range(N):
        for i in range(N):
            if (j, i) not in cache:
                visited = set([(j,i)])
                tot = 0
                cnt = 0
                start = deque([(j,i)])

                while start:
                    y, x = start.popleft()
                    tot += board[y][x]
                    cnt += 1

                    for i in range(4):
                        ny = y + dy[i]
                        nx = x + dx[i]
                        if 0 <= nx < N and 0 <= ny < N and (ny, nx) not in visited and (ny, nx) not in cache:
                            if L <= abs(board[ny][nx]-board[y][x]) <= R:
                                start.append((ny, nx))
                                visited.add((ny, nx))
                                flag = True

                change.append((tot // cnt, visited))
                cache |= visited

    for avg, pos in change:
        for y, x in pos:
            board[y][x] = avg

    if flag:
        ret += 1
    else:
        break

print(ret)