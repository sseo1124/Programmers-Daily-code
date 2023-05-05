def solution(arr, divisor):
    arr = [x for x in arr if x % divisor == 0]
    answer = sorted(arr)
    if len(arr) == 0:
        answer = [-1]
    return answer