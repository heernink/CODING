def solution(n):
    answer = 0
    start = 1
    # 자연수들로 표현 하는 방법이 여러개이므로 1부터 시작해서 방법 가짓수 세기
    while start <= n:
        total = 0
        # 1. start ~ 15까지 계속 더해주면서
        for i in range(start, n + 1):
            total += i
            # 1-1. 자연수 n을 연속한 자연수들로 표현 가능하면, 가짓수 추가하고 break걸어서 다음 시도 시작
            if total == n:
                answer += 1
                break
            # 1-2. 자연수 n보다 넘으면 표현 불가능하므로, break걸어서 다음 시도 시작
            elif total > n:
                break
        # 2. 다음 시작 번호 업데이트
        start += 1

    return answer
