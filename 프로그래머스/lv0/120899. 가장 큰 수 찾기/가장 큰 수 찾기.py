def solution(array):
    lst = []
    lst.append(max(array))
    lst.append(array.index(max(array)))
    
    return lst