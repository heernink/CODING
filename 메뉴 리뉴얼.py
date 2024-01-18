from itertools import combinations

def solution(orders, course):
    answer = []
    
    # 각 주문에서 가능한 조합 찾기
    comb = []
    for order in orders:
        order_combinations = []
        for r in range(2, len(order) + 1):
            order_combinations.extend(combinations(sorted(order), r))
        comb.extend(order_combinations)
    '''
		[('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'), ('B', 'C'), ('B', 'D'), 
    ('B', 'E'), ('C', 'D'), ('C', 'E'), ('D', 'E'), ('A', 'B', 'C'), 
    ('A', 'B', 'D'), ('A', 'B', 'E'), ('A', 'C', 'D'), ('A', 'C', 'E'),
    ('A', 'D', 'E'), ('B', 'C', 'D'), ('B', 'C', 'E'), ('B', 'D', 'E'),
    ('C', 'D', 'E'), ('A', 'B', 'C', 'D'), ('A', 'B', 'C', 'E'), 
    ('A', 'B', 'D', 'E'), ('A', 'C', 'D', 'E'), ('B', 'C', 'D', 'E'),
    ('A', 'B', 'C', 'D', 'E'), ('A', 'B'), ('C', 'D'), ('A', 'D'), ('A', 'E'), 
    ('D', 'E'), ('A', 'D', 'E'), ('X', 'Y'), ('X', 'Z'), ('Y', 'Z'), 
    ('X', 'Y', 'Z'), ('X', 'Y'), ('X', 'Z'), ('Y', 'Z'), ('X', 'Y', 'Z'),
    ('A', 'C'), ('A', 'D'), ('C', 'D'), ('A', 'C', 'D')]
		'''

    # 주문 횟수 저장을 위한 딕셔너리
    menu_count = {}
    for cb in comb:
        key = ''.join(cb)
        if key in menu_count:
            menu_count[key] += 1
        else:
            menu_count[key] = 1
    '''
		{'AB': 2, 'AC': 2, 'AD': 3, 'AE': 2, 'BC': 1, 'BD': 1, 'BE': 1, 
     'CD': 3, 'CE': 1, 'DE': 2, 'ABC': 1, 'ABD': 1, 'ABE': 1, 'ACD': 2, 
     'ACE': 1, 'ADE': 2, 'BCD': 1, 'BCE': 1, 'BDE': 1, 'CDE': 1, 'ABCD': 1, 
     'ABCE': 1, 'ABDE': 1, 'ACDE': 1, 'BCDE': 1, 'ABCDE': 1, 'XY': 2, 'XZ': 2, 
     'YZ': 2, 'XYZ': 2}
		'''

    # 각 course에 대해 가장 많이 주문된 메뉴 찾기
    for c in course:
        max_count = 2  # 최소 2명 이상의 손님에게 주문된 메뉴만 포함
        candidates = []
        
        for menu, count in menu_count.items():
						# 주문 횟수가 현재까지의 최대 주문 횟수(max_count)보다 크면, 
						# 새로운 최대 주문 횟수가 발견된 것이므로 candidates를 해당 메뉴로 업데이트하고, 
						# max_count를 새로운 값으로 업데이트
            if len(menu) == c and count >= max_count:
                if count > max_count:
                    candidates = [menu]
                    max_count = count
                else:
                    candidates.append(menu)
        
        answer.extend(candidates)
    
    return sorted(answer)
