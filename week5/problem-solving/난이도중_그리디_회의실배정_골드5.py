# 그리디 - 회의실 배정 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1931

# fix: 입력처리 없이 제출하니까 오답처리
import sys
input = sys.stdin.readline

# 회의실 리스트 초기값
N = int(input())
meetings = [0] * N

# 회의실 시간 기입 및 종료시간 기준 정렬
for i in range(N):
    meetings[i] = list(map(int, input().split()))

# 종료시간 기준 함수 (basic 문제는 일반함수로 풀었는데 lambda 함수라는게 있었음)
# meetings.sort(key=lambda x: x[1]) -> 종료시간 같은 경우 반영 안됨
meetings.sort(key=lambda x: (x[1], x[0]))   # fix: 종료시간 같은 경우, 시작시간 순으로 정렬 (튜플 비교규칙)

# 선택된 회의 리스트 설정
selected = []

# 첫번째 회의 선택
selected.append(meetings[0])

# 이후 회의 선택
for i in range(1, len(meetings)):
    if selected[-1][1] <= meetings[i][0]:
        selected.append(meetings[i])

# 가능 회의 수 출력
print(len(selected))