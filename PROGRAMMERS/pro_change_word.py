from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    visited = [False] * len(words)
    answer = 0
    q = deque([begin])

    while q:
        tmp = deque()
        current = q.popleft()
        answer += 1
        for i, next in enumerate(words):
            if not visited[i]:
                cnt = 0
                for x, y in zip(current, next):
                    if x != y:
                        cnt += 1
                if cnt == 1:
                    if target == next:
                        return answer
                    visited[i] = True
                    tmp.append(next)
        q = tmp.copy()

    return answer