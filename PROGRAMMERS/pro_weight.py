def solution(weight):
    weight.sort()
    print(weight)
    s = 1
    for i in range(len(weight)):
        if s < weight[i]:
            break
        s += weight[i]
    return s



print(solution([3, 1, 6, 2, 7, 30, 1]))