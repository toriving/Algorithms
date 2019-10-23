import copy
from itertools import product

def check():
    global board
    for y in range(h-1, 0, -1):
        for x in range(w-1, -1, -1):
            if not board[y][x]:
                for z in range(y-1, -1, -1):
                    if board[z][x]:
                        board[y][x] = board[z][x]
                        board[z][x] = 0
                        break


def drop(y, x):
    global board
    num = board[y][x]
    board[y][x] = 0

    for i in range(y-num+1, y+num):
        if i < 0 or i >= h:
            continue
        if board[i][x]:
            drop(i, x)
            board[i][x] -= num

            if board[i][x] < 0:
                board[i][x] = 0


    for i in range(x-num+1, x+num):
        if i < 0 or i >= w:
            continue
        if board[y][i]:
            drop(y, i)
            board[y][i] -= num

            if board[y][i] < 0:
                board[y][i] = 0

def find_drop(x):
    y = 0
    while True:
        if board[y][x]:
            return y,x
        y+=1

        if y >= h:
            return h-1 , x

def count(b):
    s=0
    for y in range(h):
        for x in range(w):
            if b[y][x]:
                s += 1
    return s



def step(pos):
    y, x = find_drop(pos)
    drop(y,x)
    check()

T = int(input())

for test_case in range(1, T + 1):
    ret = 987654321
    n, w, h = map(int,input().split())
    board = [list(map(int, input().split())) for _ in range(h)]
    combi = list(product(range(w),repeat=n))
    for c in combi:
        cache = copy.deepcopy(board)
        for a in c:
            step(a)
        ret = min(ret, count(board))
        board = cache

    print('#%d %d' %(test_case, ret))