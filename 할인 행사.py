import collections

def solution(want, number, discount):
    answer = 0
		# 1. 10일간 할인하는 품목의 개수를 셈
    for i in range(len(discount)-9):
        tmp = 0
				# 2. 정현이가 원하는 제품의 수량 < 10일간 할인하는 품목의 수량일 경우, tmp + 1
        for j in dict(zip(want, number)):
            if collections.Counter(discount[i:10+i])[j] >= dict(zip(want, number))[j]:
                tmp += 1
				# 3. 만약 정현이가 원하는 제품을 모두 할인 받을 수 있는 회원등록 날짜라면 answer + 1
        if tmp == len(number): answer += 1

    return answer
