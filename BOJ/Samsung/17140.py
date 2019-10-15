from collections import Counter

r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]

R = r -1
C = c -1

sec = 0

while True:
    if sec > 100:
        print(-1)
        break
    try:
        if arr[R][C] == k:
            print(sec)
            break
    except:
        pass

    sec += 1

    r = len(arr)
    c = len(arr[0])

    nr = 0
    nc = 0
    narr = []

    if r >= c:
        for ar in arr:
            tmp = []

            ct = sorted(Counter(ar).items(), key=lambda x: (x[1],x[0]))
            for x in ct:
                if x[0] == 0 or len(tmp) > 100:
                    continue
                tmp.append(x[0])
                tmp.append(x[1])
            nr = max(nr, len(tmp))
            narr.append(tmp)

        for x in narr:
            if len(x) < nr:
                x.extend([0] * (nr - len(x)))
        arr = narr

    else:

        tarr = [[0] * r for _ in range(c)]
        for i in range(r):
            for j in range(c):
                tarr[j][i] = arr[i][j]

        for ar in tarr:
            tmp = []
            ct = sorted(Counter(ar).items(), key=lambda x: (x[1],x[0]))
            for x in ct:
                if x[0] == 0 or len(tmp) > 100:
                    continue
                tmp.append(x[0])
                tmp.append(x[1])

            nr = max(nr, len(tmp))
            narr.append(tmp)

        for x in narr:
            if len(x) < nr:
                x.extend([0] * (nr - len(x)))

        arr = [[0] * len(narr) for _ in range(len(narr[0]))]
        for i in range(len(narr)):
            for j in range(len(narr[0])):
                arr[j][i] = narr[i][j]

