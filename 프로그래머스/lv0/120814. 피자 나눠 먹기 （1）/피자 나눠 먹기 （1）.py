def solution(n):
    if n % 7 == 0:
        n_pizza = n // 7
    else:
        n_pizza = n//7 + 1
    return n_pizza