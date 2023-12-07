from collections import deque

n = int(input())
a, b = map(int, input().split())  # a, b 사이의 촌수관계를 구해야 한다.
m = int(input())


def bfs(num):
    queue = deque()
    queue.append(num)
    level = 0

    while queue:
        for _ in range(len(queue)):
            value = queue.popleft()

            if value == b:
                return level

            for i in range(1, n + 1, 1):
                if graph[value][i] == 1 and visited[value][i] == 0:  # 방문하지 않은 경우
                    queue.append(i)
                    visited[value][i] = 1  # 방문 처리
                    visited[i][value] = 1  # 방문 처리
        level += 1

    return -1


# 사람들은 1, 2, ..., n
graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
visited = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

print(bfs(a))
