import sys

sys.setrecursionlimit(10 ** 6)

M, N, K = map(int, input().split())
graph = [[0] * (N) for _ in range(M)]
visited = [[False] * N for _ in range(M)]

count = 0
area = 0  # 각각의 넓이 계산
ans = []

for i in range(K):
    li = list(map(int, input().split()))
    for x in range(li[1], li[3]):
        for y in range(li[0], li[2]):
            graph[x][y] = 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    global graph, visited, area
    visited[x][y] = True
    area += 1

    for k in range(len(dx)):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] is False and graph[nx][ny] != 1:
            dfs(nx, ny)


for x in range(M):
    for y in range(N):
        if visited[x][y] is False and graph[x][y] != 1:
            count += 1
            dfs(x, y)
            ans.append(area)
            area = 0  # 넓이 초기화

print(count)
print(*sorted(ans))
