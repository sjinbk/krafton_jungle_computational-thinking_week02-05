# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157

# 단어 입력받아서 개별 글자에 대한 소문자 list, set 생성
str = input()
str_list = []
str_set = set()
for idx in range(len(str)):  
    str_list.append(str[idx].lower())
    str_set.add(str[idx].lower())

# 생성한 list, set으로 글자수를 카운팅해서 dictionary 만들기
str_dict = {}
for element in str_set:
    str_dict[element] = str_list.count(element)

# dictionary에서 최대 value값 찾기
v_max = max(str_dict.values())

# 최대 value값을 가지는 key값에 대하여 출력처리
k_max = [k for k, v in str_dict.items() if v == v_max]
if len(k_max) > 1:
    print('?')
else:
    print(k_max[0].upper())