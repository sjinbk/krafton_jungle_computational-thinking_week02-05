# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933

n = int(input())
words = []

# 단어 리스트 추가
for i in range(n):
    words.append(input())

# 단어 역순 리스트 추가
for i in range(n):
    words.append(words[i][::-1])

# 비밀번호 단어 특정하여 리스트 교체
for i in range(len(words)):
    if words.count(words[i]) > 1:
        words = words[i]
        break

# 단어 길이 및 중앙 인덱스 문자 출력
print(f"{len(words)} {words[( 0 + len(words) ) // 2]}")