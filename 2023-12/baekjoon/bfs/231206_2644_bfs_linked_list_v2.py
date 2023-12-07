from collections import deque

n = int(input())
a, b = map(int, input().split())  # a, b 사이의 촌수관계를 구해야 한다.
m = int(input())

"""
level을 사용하지 않고 visited 배열을 이용해서 증가시킨다.
이 경우, 처음에 for _ in range(len(queue)) 를 사용해서 level을 설정하지 않아도 된다.
"""


def bfs(num):
    queue = deque()
    queue.append(num)
    visited[num] = visited[num] + 1  # 방문처리

    while queue:
        value = queue.popleft()

        for k in graph[value]:
            if visited[k] == -1:  # 방문한 적이 없다면.
                queue.append(k)
                visited[k] = visited[value] + 1


# 사람들은 1, 2, ..., n
graph = [[] for _ in range(n + 1)]
visited = [-1 for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

bfs(a)
print(visited[b])
