from collections import deque


def bfs(graph):
    start_pos = [graph[0][0], graph[0][1]]
    end_pos = [graph[len(graph) - 1][0], graph[len(graph) - 1][1]]
    queue = deque()
    queue.append(start_pos)
    graph[0][2] = True  # 방문 상태 설정

    while queue:
        x, y = queue.popleft()

        # 마지막 지점에 도달이 가능하다면
        if (abs(end_pos[0] - x) + abs(end_pos[1] - y)) <= 1000:
            return 'happy'

        for i in range(1, len(graph) - 1, 1):
            if (abs(graph[i][0] - x) + abs(graph[i][1] - y)) <= 1000 \
                    and graph[i][2] is False:
                queue.append([graph[i][0], graph[i][1]])
                graph[i][2] = True

    return 'sad'


t = int(input())
answer = []
for _ in range(t):
    n = int(input())
    li = []
    for _ in range(n + 2):
        a, b = map(int, input().split())
        visited = False
        li.append([a, b, visited])  # 여기서 방문 상태를 같이 넣는다.

    answer.append(bfs(li))

for j in answer:
    print(j)
