import itertools

def solution(expression):
    answer = 0
    tmp = []
		# 1. expression을 토큰화하기
    token = ''
    for i in expression:
        if i.isdigit(): token += i
        else:
            if token:
                tmp.append(int(token))
                token = ''
            tmp.append(i)
    if token:
        tmp.append(int(token))
    
	# 2. 연산자의 순열을 구해서 순회하며 가장 큰 값을 찾는다        
    arr = ['*', '+', '-']
    nPr = itertools.permutations(arr, 3)
		# 2-1. 연산자를 순회하면서
    for i in nPr:
        cp_tmp = tmp
				# 2-2. 우선 순위대로 계산 수행
        for j in i:
            while j in cp_tmp:
                idx = cp_tmp.index(j)
                if j == "*":
                    result = cp_tmp[idx-1] * cp_tmp[idx+1]
                elif j == "+":
                    result = cp_tmp[idx-1] + cp_tmp[idx+1]
                elif j == "-":
                    result = cp_tmp[idx-1] - cp_tmp[idx+1]
                
                cp_tmp = cp_tmp[:idx-1] + [result] + cp_tmp[idx+2:]

        answer = max(answer, abs(cp_tmp[0]))
                
    return answer
