import sys

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


dy, dx = (0, 0, -1, 1), (-1, 1, 0, 0)
visited = [[False] * M for _ in range(N)]

ret = 0
def dfs(y, x, cnt, s):
    global ret
    if cnt == 4:
        ret = max(ret, s)
        return

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx]:
            visited[ny][nx] = True
            dfs(ny, nx, cnt+1, s+board[ny][nx])
            visited[ny][nx] = False

def check(ny,nx):
    return 0 <= ny < N and 0 <= nx < M


def check_fuck(y, x):
    global ret
    if (x == 0 and y == 0) or (x == 0 and y == N-1) or (x == M-1 and y == 0) or (x == M-1 and y == N-1):
        return
    candi = [ret]
    if x == 0:
        candi.append(board[y - 1][x] + board[y + 1][x] + board[y][x + 1] + board[y][x])
    elif x == M - 1:
        candi.append(board[y - 1][x] + board[y + 1][x] + board[y][x - 1] + board[y][x])
    elif y == 0:
        candi.append(board[y + 1][x] + board[y][x - 1] + board[y][x + 1] + board[y][x])
    elif y == N - 1:
        candi.append(board[y - 1][x] + board[y][x - 1] + board[y][x + 1] + board[y][x])
    else:
        candi.append(board[y-1][x] + board[y+1][x] + board[y][x+1] + board[y][x])
        candi.append(board[y - 1][x] + board[y][x-1] + board[y][x + 1] + board[y][x])
        candi.append(board[y - 1][x] + board[y + 1][x] + board[y][x - 1] + board[y][x])
        candi.append(board[y + 1][x] + board[y][x-1] + board[y][x + 1] + board[y][x])

    ret = max(candi)


for y in range(N):
    for x in range(M):
        check_fuck(y, x)
        visited[y][x] = True
        dfs(y, x, 1, board[y][x])
        visited[y][x] = False



print(ret)