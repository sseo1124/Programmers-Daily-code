def solution(numbers):
    n1 = max(numbers)
    
    numbers.remove(n1)
    
    n2 = max(numbers)
    
    answer = n1*n2
    return answer