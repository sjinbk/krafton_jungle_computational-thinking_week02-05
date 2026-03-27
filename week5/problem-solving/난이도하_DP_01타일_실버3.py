# DP - 01타일 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/1904

# 문제 풀다보니 회고까지 작성하게 만든 문제
# https://velog.io/@sjinbk/Python-%EB%A8%B8%EB%A6%AC%EA%B0%80-%EB%82%98%EC%81%98%EB%A9%B4-%EB%A9%94%EB%AA%A8%EB%A6%AC%EA%B0%80-%EA%B3%A0%EC%83%9D%ED%95%A8-%EB%8F%99%EC%A0%81%EC%9C%BC%EB%A1%9C-%EA%B3%84%ED%9A%8D-%EC%84%B8%EC%9A%B0%EA%B8%B0

n = int(input())

def tile(n):
    if n <= 2:
        return n
    
    tilearr = {1: 1, 2: 2}

    if n in tilearr:
        return tilearr[n]

    for i in range(3, n+1):
        tilearr[i] = (tilearr[i-1] + tilearr[i-2]) % 15746
    return tilearr[n]

print(tile(n))