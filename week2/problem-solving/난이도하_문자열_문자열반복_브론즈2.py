# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675

T = int(input())

for i in range(T):
    S = input()

    if S.find(" ") != -1:
        R, char = S.split()
        char_final = ""
        char_list = list(char)

        for num in range(len(char_list)):
            char_final += str(char_list[num]) * int(R)
        print(char_final)
    else:
        pass