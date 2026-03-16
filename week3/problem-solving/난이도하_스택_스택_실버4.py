# 스택 - 스택 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/10828

n = int(input())
arr = []

for i in range(n):
    cmd = input().split()
    
    if cmd[0] == 'push':
        arr.append(cmd[1])
    
    elif cmd[0] == 'pop':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop())
    
    elif cmd[0] == 'size':
        print(len(arr))

    elif cmd[0] == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)

    elif cmd[0] == 'top':
        if len(arr) == 0:
            print(-1)
        else: 
            print(arr[-1])