def solution(x):
    sum = 0
    for num in str(x):
        sum += int(num)
    if x % sum == 0:
        return True
    else:
        return False
