def solution(absolutes, signs):
    summ = 0
    for i in range(len(absolutes)):
        if signs[i] == False:
            summ += (-1*absolutes[i])
        else:
            summ += absolutes[i]
    
    return summ