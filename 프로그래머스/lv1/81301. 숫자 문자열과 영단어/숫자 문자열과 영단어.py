def solution(s):
    lst = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i, num in enumerate(lst):
        s= s.replace(num, str(i))
    
    return int(s)