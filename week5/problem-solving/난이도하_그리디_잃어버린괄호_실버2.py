# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541

import sys
input = sys.stdin.readline

# 마이너스 기준으로 분리
expr = input().strip()
parts = expr.split('-')

# 첫 마이너스 이전의 숫자합은 무조건 양수
total = sum(map(int, parts[0].split('+')))

# 첫 마이너스 이후 숫자들은 무조건 빼기
for part in parts[1:]:
    total -= sum(map(int, part.split('+')))

print(total)