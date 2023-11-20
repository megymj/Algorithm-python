# BFS 완전 기초 문제
from collections import deque

N, K = map(int, input().split())


def bfs(start):
    visited = [False] * 100001
    visited[start] = True  # 방문 체크
    queue = deque()
    queue.append(start)
    level = 0

    while queue:
        for _ in range(len(queue)):
            x = queue.popleft()
            if x == K:
                return level
            for i in [x - 1, x + 1, 2 * x]:
                if 0 <= i <= 100000 and visited[i] is False:
                    queue.append(i)
                    visited[i] = True

        level += 1


print(bfs(N))