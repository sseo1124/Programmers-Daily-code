def solution(num, k):
    num = str(num)
    
    if str(k) in num:
        answer = num.index(str(k)) + 1
    else:
        answer = -1
    return answer