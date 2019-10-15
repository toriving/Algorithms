from itertools import combinations


def distance(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

C = []
H = []

for i in range(N):
    for j in range(N):
        if MAP[i][j] == 2:
            C.append((i, j))
        elif MAP[i][j] == 1:
            H.append((i,j))

flag = [False] * len(C)

ret = 987654321
for cks in combinations(C, M):
    print(cks)
    tmp = 0
    for h in H:
        tmp2 = 987654321
        for c in cks:
            tmp2 = min(tmp2, distance(c, h))
        tmp += tmp2
    ret = min(ret , tmp)



print(ret)
