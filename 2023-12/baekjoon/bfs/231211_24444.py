import sys
from collections import deque


def bfs(num):
    global graph, visited, count
    visited[num] = count  # 방문 처리
    queue = deque()
    queue.append(num)

    while queue:
        for _ in range(len(queue)):
            x = queue.popleft()

            for val in graph[x]:
                if visited[val] == 0:  # 방문하지 않았다면
                    count += 1
                    visited[val] = count
                    queue.append(val)


N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for edge in graph:
    edge.sort()

count = 1
bfs(R)  # 시작 정점

for i in range(1, N + 1, 1):
    print(visited[i])
