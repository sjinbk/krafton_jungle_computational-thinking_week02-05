# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920

inputArray = [list(map(int, input().split())) for x in range(4)]

N = sorted(inputArray[1])
M = inputArray[3]

left = 0
right = len(N) - 1

for i in range(len(M)):
    target = M[i]
    while left <= right:
        mid = (left + right) // 2
        if N[mid] == target:
            print(1)
            left = 0
            right = len(N) - 1
            break
        elif N[mid] < target:
            left = mid + 1
        elif N[mid] > target:
            right = mid - 1
    else:
        print(0)
        left = 0
        right = len(N) - 1