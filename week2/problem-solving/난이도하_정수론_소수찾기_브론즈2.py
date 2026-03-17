# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978

import math

n = int(input())
nums = list(map(int, input().split()))
prime = []

for i in range(n):
    num = nums[i]

    if num < 2:
        continue

    if num == 2:
        prime.append(num)
        continue

    if num % 2 == 0:
        continue

    limit = int(math.sqrt(num))

    for j in range(3, limit + 1, 2):
        if num % j == 0:
            break
    else:
        prime.append(num)

print(len(prime))
