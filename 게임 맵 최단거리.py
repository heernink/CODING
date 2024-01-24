from collections import deque
def solution(maps):
		# 0. 초기 위치 queue에 담기
    que = deque()
    que.append((0,0))
		# 1. 좌,우,위,아래 이동하며 이동 가능한 길로 이동
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
		
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i] # 이동 할 길
            ny = y + dy[i] # 이동 할 길
						# 만약 이동할 길이 게임 맵 내에 있고, 1인 경우 이동 가능하므로
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] == 1:
                # 이동하며 해당 칸에 지금까지 이동한 횟수를 더해줌
								maps[nx][ny] = maps[x][y] + 1
                que.append((nx, ny))
		# 2. 만약 상대 팀 진영에 도달할 수 없을 (게임 맵 마지막 칸의 수가 1일) 경우, -1 return
    if maps[len(maps)-1][len(maps[0])-1] == 1:
        return -1
		# 도달할 경우, 가장 빠른 길 (지금까지 이동한 횟수)를 return
    else: 
        return maps[len(maps)-1][len(maps[0])-1]
