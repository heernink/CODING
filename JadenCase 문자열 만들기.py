def solution(s):
    # 1-1. 중간에 대문자가 있을 수 있으므로 모두 소문자로 미리 변경
    s = s.lower()
    # 1-2. answer에 미리 ' ' 빈칸 넣어줌
    answer = ' '

    # 2. 문자열을 하나씩 순회하며 JadenCase로 바꾸기
    for i in s:
        # 2-1. 알파벳이고 그 전 문자가 공백일 경우, 첫문자이므로 대문자로 변경
        if i.isalpha() and answer[-1] == ' ':
            answer += i.upper()
        # 2-2. 그 외의 경우 (공백이거나 첫문자가 아닌 경우), 그대로 문자 추가
        else:
            answer += i
    # 3. 처음에 answer에 미리 ' ' 빈칸 넣어주었으므로 ' ' 제외하고 출력
    return answer[1:]
