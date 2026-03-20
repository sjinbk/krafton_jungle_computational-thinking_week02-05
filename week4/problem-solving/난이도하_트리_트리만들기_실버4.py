# 트리 - 트리 만들기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/14244

n, m = map(int, input().split())

# 초기값
print("0 1")

# 리프 m개 
for i in range(2, m+1):
    print(f"1 {i}")

# 차수 2이상 노드 (n-1)-m개
if n-1-m > 0:
    for i in range(0, n-1-m):
        print(f"{m+i} {m+i+1}")