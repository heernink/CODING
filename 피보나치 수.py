def solution(n):
    # F(0) = 0, F(1) = 1 초기 설정
    a, b = 0, 1
    # 2부터 n-1까지 순회 ( 피보나치 수 : F(n) = F(n-1) + F(n-2) )
    for i in range(2, n):
        # F(n-1), F(n-2) 업데이트 
        a, b = b, a+b
        
    return (a+b)%1234567
