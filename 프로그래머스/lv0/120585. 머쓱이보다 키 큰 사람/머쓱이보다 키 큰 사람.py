def solution(array, height):
    lst = []
    for h in array:
        if h > height:
            lst.append(h)
    answer = len(lst)
    return answer