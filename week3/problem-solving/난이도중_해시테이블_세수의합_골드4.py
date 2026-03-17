# 해시 테이블 - 세 수의 합 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2295

n = int(input())

nums = []
for _ in range(n):
    nums.append(int(input()))

# x+y = k-z 가 존재하면, 이때 최대 k값 출력
x_plus_y = []
for i in range(len(nums)):
    for j in range(len(nums)):
            x_plus_y.append(nums[i] + nums[j])
x_plus_y = set(x_plus_y)


k_minus_z = []
for i in range(len(nums)):
    for j in range(len(nums)):
            if nums[i] > nums[j]:
                k_minus_z.append(nums[i] - nums[j])
k_minus_z = set(k_minus_z)

# nums.reverse() 와 구분
nums.sort(reverse=True)

for k in nums:
    for z in nums:
        if (k - z) in x_plus_y:
            print(k)
            exit()