def solution(people, limit):
    people.sort(reverse=True)

    i = 0
    j = len(people) - 1
    cnt = 0
    while i < j:
        if people[i] + people[j] <= limit:
            i += 1
            j -= 1
            cnt += 1
        else:
            i += 1

    return len(people) - cnt

solution([70,50,80,50], 100)