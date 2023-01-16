def solution(num_list):
    even_lst = []
    odd_lst = []
    for num in num_list:
        if num % 2 == 0:
            even_lst.append(num)
        elif num % 2 == 1:
            odd_lst.append(num)
    
    total_lst = []
    total_lst.append(len(even_lst))
    total_lst.append(len(odd_lst))
            
            
    return total_lst