def solution(t, p):
    answer = 0
    p_len = len(p)
    for i in range(len(t)):
        if (len(t[i:i+p_len]) == p_len) and (int(t[i:i+p_len]) <= int(p)):
            answer += 1
    return answer
        