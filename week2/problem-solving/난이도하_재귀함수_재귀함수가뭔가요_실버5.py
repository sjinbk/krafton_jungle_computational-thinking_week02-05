# 재귀함수 - 재귀함수가 뭔가요? (백준 실버5)
# 문제 링크: https://www.acmicpc.net/problem/17478

# 출력의 인코딩을 utf-8로 설정
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

def chatbot(n, count):
    # 함수 진입부
    print('____' * count + '"재귀함수가 뭔가요?"')
    # 재귀 탈출시점 (base case)
    if count == n:
        print('____' * count + '"재귀함수는 자기 자신을 호출하는 함수라네"')
    # 반복되는 부분
    else:
        print('____' * count + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
        print('____' * count + '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
        print('____' * count + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
        chatbot(n, count + 1)
    # 콜 스택 처리시점 (재귀함수 처리 후 빠져나옴)
    print('____' * count + '라고 답변하였지.')

n = int(input())
print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
chatbot(n, 0)

