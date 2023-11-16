import sys

sys.setrecursionlimit(10 ** 6)

N = int(input())
graph = [[0] * (N) for _ in range(N)]
visited = [[False] * (N + 1) for _ in range(N + 1)]

max_depth = 0
for i in range(N):
    graph[i] = list(map(int, input().split()))
    if max(graph[i]) > max_depth:
        max_depth = max(graph[i])

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(i, j):
    global depth_inc, N, graph, visited
    visited[i][j] = True

    for k in range(len(dx)):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] is False and graph[nx][ny] > depth_inc:
            dfs(nx, ny)


depth_inc = 1  # 1이상 100이하
count = 0
ans = []

while depth_inc <= max_depth:
    for x in range(N):
        for y in range(N):
            if graph[x][y] > depth_inc and visited[x][y] is False:
                count += 1
                dfs(x, y)

    ans.append(count)
    depth_inc += 1
    visited = [[False] * (N + 1) for _ in range(N + 1)]  # 초기화 필요
    count = 0

# 아무 지역도 물에 잠기지 않는 경우 => 전체 개수는 1이다.
if max(ans) == 0:
    print(1)
else:
    print(max(ans))
