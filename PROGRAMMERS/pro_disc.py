import heapq

def solution(jobs):
    answer = 0
    t = 0
    job = 0
    jobs.sort(key=lambda x: x[0])
    l = len(jobs)
    h = []
    s = 0
    flag = False

    while True:
        if not jobs and not job and not h:
            answer += t - s
            break

        if jobs:
            while jobs:
                if t == jobs[0][0]:
                    heapq.heappush(h, [jobs[0][1], jobs[0][0]])
                    jobs.pop(0)
                else:
                    break

        if job == 0 and flag:
            answer += t - s
            flag = False

        if job == 0 and h:
            job, s = heapq.heappop(h)
            flag = True

        t += 1

        if job > 0:
            job -= 1

    print(answer//l)
    return answer // l

solution([[0, 3], [1, 9], [500, 6]])
solution([[0, 3], [1, 9], [2, 6]])
solution([[0, 9], [0, 4], [0, 5], [0, 7], [0, 3]])