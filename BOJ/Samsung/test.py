
def combination(brr, cnt, r):
    if cnt == r:
        print(brr)
        return
    start = arr.index(brr[-1]) + 1 if brr else 0
    for nxt in range(start, len(arr)):
        brr.append(arr[nxt])
        combination(brr, cnt +1, r)
        brr.pop()


arr = [1,2,3,4]
combination([], 0, 3)