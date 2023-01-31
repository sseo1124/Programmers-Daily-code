def solution(rsp):
    win = ""
    for i in rsp:
        if i == '2':
            win += str(0)
        elif i == '0':
            win += str(5)
        else:
            win += str(2)
    return win