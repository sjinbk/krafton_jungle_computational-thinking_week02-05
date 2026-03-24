# 그래프, DFS, BFS - DFS와 BFS (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1260

from collections import deque

n, m ,v = map(int, input().split())
graph = {i: [] for i in range(1, n+1)}
for _ in range(m):
    a ,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# fix: 그래프 value 리스트 오름차순 배열
for key in graph:
    graph[key].sort()

# 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문

def dfs_iteration(graph, start):
    visited = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            # fix: stack 꺼낼 때 내림차순이므로 reversed 처리
            stack.extend(reversed(graph[node]))
    return visited

def bfs(graph, start):
    visited = []
    queue = deque([start])
    visited.append(start)
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    return visited

print(*dfs_iteration(graph, v))
print(*bfs(graph, v))