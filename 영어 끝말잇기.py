def solution(n, words):
	for i in range(1, len(words)):
		# 이전에 등장했던 단어는 사용할 수 없으며, 
		# 앞사람이 말한 단어의 마지막 문자로 시작하는 단어를 말해야 하는 규칙에 따라
		# 규칙을 어겼을 경우, [ 번호, 차례 ] return
		if (words[i] in words[:i]) or (words[i][0] != words[i-1][-1]):
			return [(i%n) + 1, (i//n) + 1]

		# 만약 주어진 단어들로 탈락자가 생기지 않는다면, [0, 0]을 return
    else:
      return [0, 0]
