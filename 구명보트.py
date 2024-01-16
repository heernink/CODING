from collections import deque
def solution(people, limit):
    answer = 0
		# 1. 우선 가벼운 사람 ~ 무거운 사람으로 정렬
    people.sort()

    q = deque(people)
		# 2. 큐 사람 기입한 후,
    while q:
				# 두 명이상 남아있는 경우, 가장 가벼운 사람과 무거운 사람의 몸무게 합쳐서
        if len(q) >= 2:
						# limit보다 작은 경우, 두 사람 모두 보트에 태움
            if q[0] + q[-1] <= limit:
                q.pop()
                q.popleft()
                answer += 1
						# limit보다 큰 경우, 무거운 사람 한명만 보트에 태움
            else:
                q.pop()
                answer += 1
				# 한 명만 남은 경우, 보트에 태움
        else:
            q.pop()
            answer += 1
    
    return answer
