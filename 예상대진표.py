def solution(n,a,b):
    answer = 0
		# 1. A와 B가 같은 N이 되면 해당 라운드에서 붙는 것이므로 A와 B가 다를때까지 while문 반복
    while a != b:
				# 2. 홀수일때 짝수일때 고려해서 A와 B 업데이트
        if a % 2 == 0: a = a//2
        else: a = a//2+1
        if b % 2 == 0: b = b//2
        else: b = b//2+1
				# 3. 업데이트 마다 라운드 수 추가
        answer += 1

    return answer
