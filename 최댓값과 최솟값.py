'''
| 최대값과 최솟값 (Lv2)
문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다. 
str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수, solution을 완성하세요.
예를들어 s가 "1 2 3 4"라면 "1 4"를 리턴하고, "-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.
'''

def solution(s):
    # 1. 임의로 문자열 첫번째 글자와 두번째 글자를 min, max 로 초기 설정
    min, max = int(s.split(' ')[0]), int(s.split(' ')[1])

    # 2. 문자열을 하나씩 순회하면서,
    for i in s.split(' '):
        # 2-1. max값 보다 크면 max값을 업데이트시켜주고,
        if int(i) > max:
            max = int(i)
        # 2-2. min값 보다 작으면 min값을 업데이트 시켜준다
        elif int(i) < min:
            min = int(i)
    
    return str(min)+ ' '+ str(max)
