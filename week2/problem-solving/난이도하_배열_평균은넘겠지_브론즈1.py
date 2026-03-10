# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344

# 처음 받은 정수 input값만큼 반복
C = int(input())
for n in range(C):
    # 입력 받아서 슬라이싱하고 학생 수, 점수로 나눔
    input_list = [int(x) for x in input().split()]
    N = input_list[:1]
    score = input_list[1:]
    # 점수를 모두 더하고 학생 수로 나눠서 평균점수 구하기
    avg_score = sum(score)/sum(N)
    # 평균점수보다 높은 학생 수 구하기
    above_score = [x for x in score if x > avg_score]
    # (백분율 %) = (평균보다 높은 학생 수)/(전체 학생 수)*100
    percent = len(above_score)/len(score) * 100    
    print(f"{percent:.3f}%")