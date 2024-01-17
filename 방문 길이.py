def solution(dirs):
		# 1. (0, 0) 에서 출발, 방향 설정, 지나가는 길 route에 담아주기
    x, y = (0, 0)
    dic = dict(zip(['R', 'U', 'L', 'D'],  [(1, 0), (0, 1), (-1, 0), (0, -1)]))
    route = []
		# 2. 지나가는 길 순회하면서
    for l in dirs:
				# 2-1. 좌표평면의 경계를 넘어가는 명령어는 무시하면서, 
        if -5 <= x+dic[l][0] <= 5 and -5 <= y+dic[l][1] <= 5:
						# 2-2. 출발 지점 --> 도착 지점 / 도착 지점 --> 출발 지점 지나간 길 리스트에 담아주기
            route.append(((x, y), (x+dic[l][0], y+dic[l][1])))
            route.append(((x+dic[l][0], y+dic[l][1]), (x, y)))
						# 2-3. 현재 위치 업데이트
            x, y = x+dic[l][0], y+dic[l][1]
		# 3. set함수 사용해서 이미 지나온 길 제거
    return len(set(route)) // 2
