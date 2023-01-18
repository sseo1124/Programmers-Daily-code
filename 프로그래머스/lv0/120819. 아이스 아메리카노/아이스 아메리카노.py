def solution(money):
    n_cof = money //5500
    exchange = money - n_cof*5500
    return [n_cof, exchange]