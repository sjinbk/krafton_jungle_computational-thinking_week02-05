# 그리디 - 동전 0 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/11047

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
# 동전 리스트 내림차순 정렬
coins.sort(reverse=True)

def greedy_coin(n, k):
    total_coins_cnt = 0
    
    # 남은 금액에 대하여 위 과정 반복
    while k > 0:
        best_coin = 0
        for i in range(n):
            if coins[i] <= k:
                # 전체 금액과 제일 차이가 적은 동전 종류를 구한다
                best_coin = coins[i]
                break
        # 해당 동전 종류로 목표 금액을 넘지않는 최대 개수를 구한다
        count = k // best_coin
        total_coins_cnt += count
        k %= best_coin
    print(total_coins_cnt)

greedy_coin(n, k)