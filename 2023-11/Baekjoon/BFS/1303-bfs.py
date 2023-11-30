"""
기초적인 BFS 문제
방향이 이전 문제들과 다르다.
N: 가로, M: 세로
"""

from collections import deque

N, M = map(int, input().split())
graph = []
visited = [[0] * (N) for _ in range(M)]

for _ in range(M):
    graph.append(list(map(str, input())))


def bfs(x, y):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    visited[x][y] = 1  # 방문 처리
    symbol = graph[x][y]
    queue = deque()
    queue.append([x, y])
    count = 1

    while queue:
        a, b = queue.popleft()

        for k in range(4):
            nx = a + dx[k]
            ny = b + dy[k]
            if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == symbol \
                    and visited[nx][ny] == 0:
                queue.append([nx, ny])
                count += 1
                visited[nx][ny] = 1  # 방문 처리

    return count


B_counts = 0
W_counts = 0

for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:
            if graph[i][j] == 'W':
                W_counts += bfs(i, j) ** 2
            else:
                B_counts += bfs(i, j) ** 2

print(W_counts, B_counts)
