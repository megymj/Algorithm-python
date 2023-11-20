"""
level 3: 네트워크
"""
import sys

sys.setrecursionlimit(10 ** 6)


def solution(n, computers):
    answer = 0
    visited = [0] * n

    # 0부터 n-1까지 전체를 탐색해야 함
    for i in range(0, n, 1):
        if visited[i] == 0:  # 방문하지 않았으면
            dfs(i, computers, visited, n)
            answer += 1

    return answer


def dfs(num, graph, checked, n):
    checked[num] = 1  # 방문 체크

    for j in range(0, n, 1):
        if graph[num][j] == 1 and checked[j] != 1:
            dfs(j, graph, checked, n)


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
