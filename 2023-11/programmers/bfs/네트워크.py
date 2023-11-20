"""
level 3: 네트워크
"""
from collections import deque


def solution(n, computers):
    answer = 0
    visited = [0] * n
    queue = deque()

    # 결론적으로 인덱스 0부터 n까지 모두 탐색해야 한다. 네트워크 수를 모두 찾아야 하므로
    for i in range(0, n, 1):
        if visited[i] == 0:  # 방문하지 않았다면
            bfs(n, computers, i, visited)
            answer += 1

    return answer


def bfs(n, computers, num, visited):
    visited[num] = 1  # 방문 처리
    queue = deque()
    queue.append(num)

    while queue:
        for _ in range(len(queue)):
            x = queue.popleft()
            for j in range(0, n, 1):
                if computers[x][j] == 1 and visited[j] != 1:
                    queue.append(j)
                    visited[j] = True


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
