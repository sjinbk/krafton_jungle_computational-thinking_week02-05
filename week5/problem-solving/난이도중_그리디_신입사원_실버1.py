# 그리디 - 신입 사원 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1946

import sys
input = sys.stdin.readline

test_case = int(input())

# 함수로 묶어서 test case별 반복
def applicant_max():
    applicant_num = int(input())
    applicant_scores = [0] * applicant_num

    for i in range(applicant_num):
        applicant_scores[i] = list(map(int, input().split()))
    
    # 서류 성적 기준으로 정렬
    applicant_scores.sort()

    # 서류 최고점자 면접 점수 기준으로 전체 순회
    cnt = applicant_num
    for i in range(applicant_num):
        # 낮으면 탈락
        if applicant_scores[0][1] < applicant_scores[i][1]:
            cnt -= 1
        # 서류 최고점자보다 면접 점수 높은 경우 
        elif applicant_scores[0][1] > applicant_scores[i][1]:
        # 생존자 그대로, 최저점을 변경
            applicant_scores[0][1] = applicant_scores[i][1]
    
    return cnt

# 입력에 대한 출력
for _ in range(test_case):
    print(applicant_max())


"""
[초기 아이디어]
# 떨어진다 -> 두 가지 성적 중 모두 낮음
# if 이 사람보다 서류 점수가 낮은 사람이 있는가?:
#   없다면 break
#   있다면 if 이 사람보다 면접 점수가 낮은 사람이 있는가?:
#       없다면 return 합격인원 += 1
#       있다면 return

# 리스트 내에서 내가 아닌 다른 사람을 고르는 방법
# 아니면 아예 리스트로 접근하면 안되나?
# 애초에 나 자신은 동점이니까 그냥 리스트 전체로 돌려도 되나
# 근데 그러면 O(n^2)
"""