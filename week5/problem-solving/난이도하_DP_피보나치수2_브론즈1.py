# DP - 피보나치 수 2 (백준 브론즈 1)
# 문제 링크: https://www.acmicpc.net/problem/2748

# basic 문제에서 하향식 해봤으니까 상향식(tabulation)으로 풀어보기

# 입력 받기
n = int(input())

# 피보나치 함수에 대하여
def fib(n):
# 점화식 초기항 처리
    if n <= 1:
        return n
# 배열 생성 및 초기화
    fibtab = {1: 1, 2: 1}
# 점화식에 대하여 작은 문제부터 차례로 계산
    for i in range(3, n+1):
        fibtab[i] = fibtab[i-1] + fibtab[i-2]
    
    return fibtab[n]

print(fib(n))