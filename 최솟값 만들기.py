def solution(A,B):
    answer = 0
    lst = []
    
    for a in A:
        tmp = []
        for b in B:
            tmp.append(a*b)
        lst.append(sorted(tmp, reverse=True))

    for i in range(len(lst)):
        tmp = []
        for j in range(len(lst)):
            tmp.append(lst[j][i])
        answer += min(tmp)
        lst.pop(tmp.index(min(tmp)))
        
    return answer
