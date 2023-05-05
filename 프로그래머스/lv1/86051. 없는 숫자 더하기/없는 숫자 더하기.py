def solution(numbers):
    num_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    answer = sum(list(set(num_lst) - set(numbers)))
    return answer