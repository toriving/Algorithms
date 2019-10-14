N = int(input())
S = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0] * N

#for i in range(N):
#     if i + S[i][0] <= N:
#         dp[i] = S[i][1]
#         for j in range(i):
#             if j + S[j][0] <= i:
#                 dp[i] = max(dp[i], dp[j] + S[i][1])

ret = 0

def solve(day, s):
    global ret
    if day == N:
        ret = max(ret, s)
        return

    if day > N:
        return

    solve(day + S[day][0], s + S[day][1])
    solve(day+1, s)

solve(0, 0)
print(ret)

# print(dp)
# print(max(dp))