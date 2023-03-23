def solution(before, after):
    before_lst = sorted([char for char in before])
    after_lst = sorted([char for char in after])
    
    before = ''
    for char in before_lst:
        before += char
    
    after = ''
    for char in after_lst:
        after += char
    
    if before == after:
        answer = 1
    else:
        answer = 0
    return answer