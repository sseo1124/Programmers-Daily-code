def solution(dot):
    if dot[0] > 0 and dot[1] > 0:
        result = 1
    elif dot[0] < 0 and dot[1] > 0:
        result = 2
    elif dot[0] < 0 and dot[1] < 0:
        result = 3
    else:
        result = 4
    return result