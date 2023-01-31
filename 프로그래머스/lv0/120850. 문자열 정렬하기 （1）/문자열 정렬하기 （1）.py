def solution(my_string):
    num_lst = []
    for num in my_string:
        if num in [str(i) for i in range(10)]:
            num_lst.append(int(num))
    num_lst.sort()
    return num_lst

            