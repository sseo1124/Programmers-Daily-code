def solution(s1, s2):
    com_lst = []
    
    for i in s1:
        for j in s2:
            if i == j:
                com_lst.append(i)
    return len(com_lst)