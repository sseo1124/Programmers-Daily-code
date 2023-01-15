def solution(n):
    lst = []
    for even in range(n+1):
        if even % 2 == 0:
            lst.append(even)
    total =sum(lst)
            
    return total