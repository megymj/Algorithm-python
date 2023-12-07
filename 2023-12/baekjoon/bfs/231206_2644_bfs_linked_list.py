from collections import deque

n = int(input())
a, b = map(int, input().split())  # a, b 사이의 촌수관계를 구해야 한다.
m = int(input())


def bfs(num):
    queue = deque()
    queue.append(num)
    visited[num] = 1  # 방문처리
    level = 0

    while queue:
        for _ in range(len(queue)):
            value = queue.popleft()

            if value == b:
                return level

            for k in graph[value]:
                if visited[k] == 0:
                    queue.append(k)
                    visited[k] = 1

        level += 1

    return -1


# 사람들은 1, 2, ..., n
graph = [[] for _ in range(n + 1)]
# visited = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

print(bfs(a))
