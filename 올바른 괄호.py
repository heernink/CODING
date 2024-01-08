def solution(s):
    stack = []
    # 문자열을 순회하며 탐색
    for i in s:
        # 1. 먼저 (이면 stack에 넣기
        if i == '(': 
            stack.append(i)
        # 2. )이면 
        else:
            # 2-1. stack에 (가 있으면
            if stack:
                # 올바른 괄호이므로 ( pop!
                stack.pop()
            # 2-2. stack이 비어있으면
            else:
                # 올바른 괄호가 아니므로 False 리턴
                return False
    # 3. 문자열 모두 순회한 뒤, stack에 문자열이 남겨진 경우,
    if stack:
        # 올바른 괄호가 아닌 것이 남겨져있는 것이므로 False 리턴
        return False
    # stack에 문자열이 없는 경우,
    else:
        # 문자열 모두가 올바른 괄호이므로 True 리턴
        return True
