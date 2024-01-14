from itertools import permutations
# 1. 소수인지 판별 함수 만들기
def sosu(n):
    if n < 2: return False # 0과 1은 소수가 아님
    for i in range(2, n // 2 + 1):
        if n % i == 0: # 나눠지면 소수가 아님
            return False
    return True

def solution(numbers):
    answer = []
    lst = set()
		# 2. numbers 가능한 조합 수 만들어서 lst에 업데이트하기
    for i in range(1, len(numbers) + 1):
        lst.update(set(permutations(list(numbers), i)))
		# 3. lst에 있는 숫자 순회하며 소수인지 판별, 소수이면 answer에 append
    for j in lst:
        if sosu(int(''.join(j))):
            answer.append(int(''.join(j)))
    return len(set(answer))
