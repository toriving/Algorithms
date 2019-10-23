from collections import deque

T = int(input())

dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)

def cost(k):
    return k*k + (k-1)*(k-1)

for tc in range(1, T+1):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    ret = 0

    for y in range(n):
        for x in range(n):
            visited = [[False] * n for _ in range(n)]
            house = 0
            q = deque()
            q.append((y,x))
            visited[y][x] = True

            house += board[y][x]
            serv = 1

            while q:
                if serv > n*2:
                    break
                if house * m - cost(serv) >= 0:
                    ret = max(ret, house)

                for _ in range(len(q)):
                    cy, cx = q.popleft()
                    for i in range(4):
                        nx = cx + dx[i]
                        ny = cy + dy[i]

                        if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[ny][nx]:
                            continue

                        visited[ny][nx] = True
                        q.append((ny,nx))
                        house += board[ny][nx]

                serv += 1


    print('#%d %d' %(tc,ret))