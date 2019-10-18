import math
n = int(input())
a = list(map(int, input().split()))
b, c = map(int,input().split())

a = [math.ceil((x - b)/c) + 1 if x-b > 0 else 1 for x in a]
print(sum(a))
