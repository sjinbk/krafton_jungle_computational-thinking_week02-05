# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865

import sys
input = sys.stdin.readline

# n: 물건의 개수
# k: 버틸 수 있는 최대 무게
n, k = map(int, input().split())

# 물건 정보를 저장할 리스트
# 각 원소는 [무게, 가치]
items = []

for _ in range(n):
    w, v = map(int, input().split())
    items.append((w, v))

# dp[i][j]
# -> i번째 물건까지 고려했을 때,
#    배낭 허용 무게가 j일 때 얻을 수 있는 최대 가치
dp = [[0] * (k + 1) for _ in range(n + 1)]

# 1번 물건부터 n번 물건까지 차례대로 고려
for i in range(1, n + 1):
    weight = items[i - 1][0]   # 현재 물건의 무게
    value = items[i - 1][1]    # 현재 물건의 가치

    # 배낭 허용 무게를 1부터 k까지 순회
    for j in range(1, k + 1):
        # 현재 물건의 무게가 허용 무게보다 크면
        # 이 물건은 넣을 수 없음
        if weight > j:
            # 이전 물건들까지만 고려한 값 그대로 사용
            dp[i][j] = dp[i - 1][j]

        # 현재 물건을 넣을 수 있다면
        else:
            # 1. 현재 물건을 넣지 않는 경우
            not_take = dp[i - 1][j]

            # 2. 현재 물건을 넣는 경우
            #    현재 물건 무게만큼 뺀 나머지 공간에서
            #    이전 물건들로 만들 수 있는 최대 가치 + 현재 물건 가치
            take = dp[i - 1][j - weight] + value

            # 둘 중 더 큰 값을 선택
            dp[i][j] = max(not_take, take)

# n개의 물건까지 고려했고,
# 최대 허용 무게가 k일 때의 최대 가치 출력
print(dp[n][k])