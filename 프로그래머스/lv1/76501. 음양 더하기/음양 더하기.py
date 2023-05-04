def solution(absolutes, sign):
    sum = 0
    for num, char in zip(absolutes, sign):
        if char:
            num = num
        else:
            num = - num 
        sum += num

    answer = sum
    return answer