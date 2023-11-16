from collections import deque

n, m = map(int, input().split())
# graph = [[0 for _ in range(n)] for _ in range(m)]
# visited = [[False] * n for _ in range(m)] # 이번에는 visited 배열을 사용하지 않고 풀어보자.
graph = []

for i in range(n):
    li = list(map(int, input().split()))
    graph.append(li)

count = 0
max_area = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    global m, n, graph
    graph[x][y] = 0
    queue = deque()
    queue.append([x, y])
    sum_area = 1  # 1부터 시작해야함.

    while queue:
        for i in range(len(queue)):
            x, y = queue.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                    sum_area += 1
                    queue.append([nx, ny])
                    graph[nx][ny] = 0

    return sum_area


for x in range(n):
    for y in range(m):
        if graph[x][y] == 1:
            max_area = max(bfs(x, y), max_area)
            count += 1

print(count)
print(max_area)
