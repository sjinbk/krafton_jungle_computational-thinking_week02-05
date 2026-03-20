# 트리 - 상근이의 여행 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/9372

# 비행기 스케줄은 항상 연결 그래프 : m >= n-1
# 모든 노드를 연결하기 위한 최소 간선 수 : n-1

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    for _ in range(m):
        input()
    print(n - 1)