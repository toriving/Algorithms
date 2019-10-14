def check(road):
    current = road[0]
    visited = [False] * N

    for i, r in enumerate(road):
        if current == r:
            continue

        elif current + 1 == r:
            for j in range(i - 1, i - 1 - L, -1):
                if j < 0 or current != road[j] or visited[j] == True:
                    return False
                visited[j] = True
            current = r

        elif current - 1 == r:
            for j in range(i, i + L):
                if j >= N or current - 1 != road[j] or visited[j] == True:
                    return False
                visited[j] = True
            current = r

        else:
            return False

    return True


def solve():
    global ret
    for x in MAP:

        ret += check(x)

    for x in range(N):
        c = list(MAP[y][x] for y in range(N))

        ret += check(c)


N, L = map(int,input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
ret = 0

solve()
print(ret)
