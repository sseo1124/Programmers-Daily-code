def solution(food):
    answer = str()
    for idx, num in enumerate(food):
        if num // 2 != 0:
            batch_num = num//2
            answer += str(idx)*batch_num
        else:
            continue
    reverse = answer[::-1]
    answer = answer + '0' + reverse
    return answer
            
        