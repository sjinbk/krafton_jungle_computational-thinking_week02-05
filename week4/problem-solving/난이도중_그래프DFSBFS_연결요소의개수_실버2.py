# 그래프, DFS, BFS - 연결 요소의 개수 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11724

# fix: 제출 시 시간초과나서 추가
import sys
input = sys.stdin.readline

# 입력 받아서 무방향 인접 리스트 만들기
n, m = map(int, input().split())
graph = {i: [] for i in range(1, n+1)}
for _ in range(m):
    u ,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# dfs 함수 선언
def dfs_iteration(graph, start, visited):
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            stack.extend(graph[node])

# 카운팅 변수, 탐색결과 정의
count = 0
visited = set()

# 그래프 전체 노드에 대해서 탐색결과 중복 안되면 카운트 증가
for node in range(1, n+1):
    if node not in visited:
        dfs_iteration(graph, node, visited)
        count += 1

print(count)