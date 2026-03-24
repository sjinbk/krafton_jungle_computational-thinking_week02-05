# 트리 - 트리의 부모 찾기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11725

# 인접 리스트 생성
n = int(input())

graph = {i:[] for i in range(1, n+1)}

for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 넓이 탐색으로 각 노드에 대한 레벨 순서 리스트 만들기
# BFS로 방문 순서 기록 + 부모 동시에 기록
from collections import deque
def bfs(graph, start):
    parent = [0] * (n+1)
    visited = [False] * (n+1)
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                # 큐에 올라가는 순서는 인접 리스트 기준으로 레벨 단위로 가므로 새롭게 큐에 추가되는 노드가 자식노드
                parent[neighbor] = node
                queue.append(neighbor)

    return parent

parent = bfs(graph, 1)

for node in range(2, n+1):
    print(parent[node])