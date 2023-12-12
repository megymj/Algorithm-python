import sys

sys.setrecursionlimit(10 ** 6)


def dfs(x, y):
    global graph, visited, count, w, h
    dx = [1, 1, 0, -1, -1, -1, 0, 1]  # 6시 -> 9시 -> 12시 -> 3시
    dy = [0, -1, -1, -1, 0, 1, 1, 1]
    visited[x][y] = 1  # 방문 처리

    for k in range(8):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1 and visited[nx][ny] == 0:
            dfs(nx, ny)


answer = []
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    # w가 세로, h가 가로
    graph = []
    visited = [[0] * (w) for _ in range(h)]
    count = 0
    for _ in range(h):
        graph.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and visited[i][j] == 0:
                dfs(i, j)
                count += 1

    answer.append(count)

for c in answer:
    print(c)
