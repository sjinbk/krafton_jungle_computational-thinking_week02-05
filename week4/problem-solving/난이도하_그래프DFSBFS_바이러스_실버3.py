# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606

from collections import deque

# 1. 입력값 받아서 인접 리스트 만들기
computer = int(input())
graph_num = int(input())

graph = { i: [] for i in range(1, computer + 1) }
for _ in range(graph_num):
    k, v = map(int, input().split())
    graph[k].append(v)
    graph[v].append(k)

# 2. 인접 리스트에 대한 bfs 함수 만들기
def bfs(graph, start):
    visited = [start]
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        for neighbor_node in graph[node]:
            if neighbor_node not in visited:    # 시간 복잡도 감소시키기 위해 -> index 접근해보기 또는 set 함수
                queue.append(neighbor_node)
                visited.append(neighbor_node)
    # 3. bfs 함수 return 값을 visited 큐에 대한 길이로 받기 (자기자신은 제외하므로 -1)
    return len(visited) - 1

print(bfs(graph, 1))