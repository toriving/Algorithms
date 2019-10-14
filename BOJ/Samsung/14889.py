from itertools import combinations, permutations

def solve():
    global ret
    cb = list(combinations(range(N), N//2))
    A = cb[:len(cb)//2]
    B = cb[len(cb)//2:][::-1]



    for i in range(len(A)):
        As = list(permutations(A[i], 2))
        Bs = list(permutations(B[i], 2))
        score_a = 0
        score_b = 0
        for x, y in As:
            score_a += MAP[x][y]
        for x, y in Bs:
            score_b += MAP[x][y]

        ret = min(ret, abs(score_a - score_b))


N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
ret = 987654321

solve()
print(ret)