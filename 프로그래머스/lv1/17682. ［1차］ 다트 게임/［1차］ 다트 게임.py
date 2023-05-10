def solution(dartResult):
    dartResult = dartResult.replace('10', 't')
    dic = {'S': 1, 'D': 2, 'T': 3}
    point = ['10' if result == 't' else result for result in dartResult]
    answer = []
    for result in point:
        if result in dic:
            answer[-1] = answer[-1] ** dic[result]
        elif result == '*':
            try: 
                answer[-2] = answer[-2] * 2      
                answer[-1] = answer[-1] * 2
            except:
                answer[-1] = answer[-1] * 2
        elif result == '#':
            answer[-1] = answer[-1] * -1
        else:
            answer.append(int(result))
    return sum(answer)
