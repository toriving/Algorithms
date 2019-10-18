from collections import deque
import copy

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
q = deque()

ret = 0

def find(y, x):
    if board[y][x]:
        q.append(board[y][x])
        board[y][x] = 0

def block_sum(y, x, dy, dx):
    while q:
        e = q.popleft()
        if not board[y][x]:
            board[y][x] = e
        elif board[y][x] == e:
            board[y][x] = e * 2
            y, x = y + dy, x + dx
        else:
            y, x = y + dy, x + dx
            board[y][x] = e

def move(dir):
    # 상 하 좌 우
    if dir == 0:
        for x in range(n):
            for y in range(n):
                find(y, x)
            block_sum(0, x, 1, 0)

    elif dir == 1:
        for x in range(n):
            for y in range(n-1, -1, -1):
                find(y, x)
            block_sum(n-1, x, -1, 0)

    elif dir == 2:
        for y in range(n):
            for x in range(n):
                find(y, x)
            block_sum(y, 0, 0, 1)

    else:
        for y in range(n):
            for x in range(n-1, -1, -1):
                find(y,x)
            block_sum(y, n-1, 0, -1)

def dfs(cnt):
    global board, ret
    if cnt == 5:
        for i in range(n):
            ret = max(ret, max(board[i]))
        return
    tmp = copy.deepcopy(board)

    for dir in range(4):
        move(dir)
        dfs(cnt+1)
        board = copy.deepcopy(tmp)

dfs(0)
print(ret)