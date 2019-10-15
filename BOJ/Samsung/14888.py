from itertools import permutations

N = int(input())
A = list(map(int, input().split()))
op = list(map(int, input().split()))
min_ = 987654321
max_ = -987654321

operation = {0:'+', 1:'-', 2: '*', 3:'/'}
opl = []

for i in range(4):
    for j in range(op[i]):
        opl.append(i)

opl = set(list(permutations(opl, N-1)))


for x in opl:
    s = str(A[0])
    for i, o in enumerate(x):
        s += operation[o]
        s += str(A[i+1])
        s = str(int(eval(s)))

    min_ = min(min_, int(s))
    max_ = max(max_, int(s))

print(max_)
print(min_)
