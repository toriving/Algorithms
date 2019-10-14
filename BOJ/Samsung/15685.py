def check():
    global ret
    for i in range(100):
        for j in range(100):
            if BG[i][j] and BG[i][j+1] and BG[i+1][j] and BG[i+1][j+1]:
                ret += 1

N = int(input())

BG = [[0] * 101 for _ in range(101)]
dy, dx = (0, -1, 0, 1), (1, 0, -1, 0)

ret = 0
gdir = [0]


for i in range(1, 11):
    k = 1 << (i-1)
    for j in range(k):
        gdir.append((gdir[k-j-1] +1) %4)

for _ in range(N):
    x, y, d, g = map(int, input().split())
    BG[x][y] = 1
    for i in range(1<<g):
        x, y = x+dx[(gdir[i]+d)%4], y+dy[(gdir[i]+d)%4]
        BG[x][y] = 1

check()
print(ret)


