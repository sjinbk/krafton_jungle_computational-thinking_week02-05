# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173

# 게임판 설정
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# 젤리 이동 과정
def dfs(x, y):
    # 게임판 밖으로 나가면 실패
    if x >= n or y >= n:
        return False

    # 현재 칸이 도착 지점이면 성공
    if board[x][y] == -1:
        return True

    # 아직 게임판 내부라면 현재 위치의 이동 세기값 받아오기
    jump = board[x][y]

    # [fix : 런타임 에러 (RecursionError)] 게임판이 0 이면 이동불가이므로 게임 종료
    if jump == 0:
        return False

    # 오른쪽 이동 또는 아래 이동 중 하나라도 성공하면 True
    return dfs(x + jump, y) or dfs(x, y + jump)

if dfs(0, 0):
    print("HaruHaru")
else:
    print("Hing")