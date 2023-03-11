def solution(array, n):
    array.sort()
    sub = [abs(i-n) for i in array] 
        
    temp = min(sub)
    
    res = [i for i, j in enumerate(sub) if j == temp]
    
    idx = res[0]
    
    answer = array[idx]
    return answer