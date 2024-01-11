def solution(s):
		# 0. 스택 이용
    stack = []
		# 1. 문자열 순회하면서
    for i in s:
				# 1-1. 같은 알파벳이 2개 붙어 있는 짝이면, 담겨있던 알파벳 제거 및 추가하지 않기
        if stack and i == stack[-1]: 
            stack.pop()
				# 1-2. 담겨있던 알파벳과 i 가 다른 알파벳이면, 새로운 알파벳 i 추가
        else:
            stack.append(i)
    # 2. 빈 스택이면 모두 짝이므로, return 1        
    if not stack: 
        return 1
		# 그렇지 않으면 return 0
    return 0
