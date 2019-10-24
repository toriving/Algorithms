def solution(n, costs):
    answer = 0
    visited = [False] * n
    costs.sort()
    visited[costs[0][0]] = True
    while sum(visited) != n:
        m = 987654321
        i = 0
        for j in range(len(costs)):
            if visited[costs[j][0]] and visited[costs[j][1]]:
                continue

            if (visited[costs[j][0]] or visited[costs[j][1]]) and costs[j][2] < m:
                m = costs[j][2]
                i = j

        answer += m
        visited[costs[i][0]] = True
        visited[costs[i][1]] = True
        costs.pop(i)

    return answer