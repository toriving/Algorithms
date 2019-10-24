

T = int(input())

for tc in range(1, T+1):
    n, m, k, a, b = map(int,input().split())
    a_t = list(map(int, input().split())) # 창구 접수 시간
    b_t = list(map(int, input().split())) # 정비 시간
    p_t = list(map(int, input().split())) # 방문시간

    # n = 접수 개수, m = 정비 개수, k = 고객 수 , a : 접수 번호, b: 정비 번호

    recep = [0] * n
    fix = [0] * m
    recep_lst = [[] for _ in range(n)]
    fix_lst = [[] for _ in range(m)]

    t = 0
    p = 0
    waiting_a = []
    waiting_f = []
    end = []
    while True:

        while t in p_t:
            waiting_a.append(p)
            p += 1
            p_t.remove(t)

        if len(end) == k:
            break

        for i in range(n):
            if recep[i]:
                recep[i] -= 1
                if not recep[i]:
                    waiting_f.append(recep_lst[i][-1])

        for i in range(m):
            if fix[i]:
                fix[i] -= 1
                if not fix[i]:
                    end.append(fix_lst[i][-1])

        for i in range(n):
            if not recep[i] and waiting_a:
                recep[i] = a_t[i]
                recep_lst[i].append(waiting_a.pop(0))


        for i in range(m):
            if not fix[i] and waiting_f:
                fix[i] = b_t[i]
                fix_lst[i].append(waiting_f.pop(0))

        t += 1


    tmp = set(recep_lst[a-1]) & set(fix_lst[b-1])
    ret = sum(tmp) + len(tmp)
    if ret == 0:
        ret = -1
    print('#%d %d' %(tc, ret))
