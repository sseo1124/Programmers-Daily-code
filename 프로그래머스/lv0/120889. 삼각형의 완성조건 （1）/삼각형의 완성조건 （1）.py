def solution(sides):
    sides.sort(reverse = True)
    
    if sides[0] < sum(sides[1:]):
        answer = 1
    else:
        answer = 2
    
    return answer