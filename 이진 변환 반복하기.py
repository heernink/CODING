# 1. 이진 변환하는 함수 만들기
def two(l):
    answer = ''
    while l != 1:
        answer += str(l % 2)
        l = l // 2
    answer += '1'
    return answer[::-1] # 역수 반환

def solution(s):
    answer = [0, 0]
    # s가 1이 될때까지 수행
    while s != '1':
        # 1. x의 모든 0을 제거하고 제거된 모든 0의 개수 구하기
        answer[1] += s.count("0")
        s = s.replace("0", "")
        # 2. x의 길이를 c라고 하면, x를 "c를 2진법으로 표현한 문자열"로 바꾸고, 변환 횟수 추가하기
        s = two(len(s))
        answer[0] += 1

    return answer
