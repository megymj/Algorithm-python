"""
기초적인 DFS 문제
방향이 이전 문제들과 다르다.
N: 가로, M: 세로
"""

N, M = map(int, input().split())
graph = []
visited = [[0] * (N) for _ in range(M)]

for _ in range(M):
    graph.append(list(map(str, input())))


def dfs(x, y, count):
    visited[x][y] = 1  # 방문 체크
    symbol = graph[x][y]
    count += 1
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == symbol \
                and visited[nx][ny] == 0:
            count = dfs(nx, ny, count)  # count를 누적해서 더한다.

    return count


B_counts = 0
W_counts = 0

for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:
            if graph[i][j] == 'W':
                W_counts += dfs(i, j, 0) ** 2
            else:
                B_counts += dfs(i, j, 0) ** 2

print(W_counts, B_counts)
