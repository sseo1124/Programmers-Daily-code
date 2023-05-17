def solution(X, Y):
    answer = ''
    # 가장 큰 9부터 시작해서 점점 작은 숫자를 더해주면 가장 큰수가 나온다 (Greedy)
    for i in range(9, -1, -1):
        x_cnt = X.count(str(i)) 
        y_cnt = Y.count(str(i))
        common_cnt = min(x_cnt, y_cnt) # 중복이 아닌경우는 0이 나와서 0을 곱해서 str에 아무것도 안더해진다
        answer += str(i)*common_cnt
    if answer == '':
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else:
        return answer