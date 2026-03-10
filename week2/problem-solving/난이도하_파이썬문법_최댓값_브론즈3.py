# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562

nums = []
for _ in range(9):
    nums.append(int(input()))

print(
    max(nums)
)

print(
    nums.index(max(nums)) + 1
)