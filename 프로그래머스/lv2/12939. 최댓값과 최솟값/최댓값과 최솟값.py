def solution(s):
    elem_lst = s.split(' ')
    lst = [int(num) for num in elem_lst]
    max_val = max(lst)
    min_val = min(lst)
    answer = str(min_val) + ' ' + str(max_val)
    return answer