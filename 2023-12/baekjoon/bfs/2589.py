from collections import deque

L, W = map(int, input().split())
graph = []

for _ in range(L):
    graph.append(list(map(str, input())))


def bfs(x, y, visited):
    global graph, L, W
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visited[x][y] = 1  # 방문 처리
    queue = deque()
    queue.append([x, y])
    level = 0

    while queue:
        for _ in range(len(queue)):
            a, b = queue.popleft()
            for k in range(4):
                nx = a + dx[k]
                ny = b + dy[k]
                if 0 <= nx < L and 0 <= ny < W and visited[nx][ny] == 0 \
                        and graph[nx][ny] == 'L':
                    queue.append([nx, ny])
                    visited[nx][ny] = 1  # 방문 처리
        level += 1

    return level - 1
    # queue에서 마지막을 돌 때, 더이상 갈 곳이 없으면 종료되면서 동시에 level += 1을 하므로,
    # -1을 통해 1 감소시켜야 한다.


answer = 0
for i in range(L):
    for j in range(W):
        # 육지인 경우만 고려한다.
        if graph[i][j] == 'L':
            # 보물섬이 묻혀있는 두 곳을 모르기 때문에, 매번 새로운 방문 체크 배열을 사용해야 한다.
            visited = [[0 for _ in range(W)] for _ in range(L)]
            answer = max(answer, bfs(i, j, visited))

print(answer)
