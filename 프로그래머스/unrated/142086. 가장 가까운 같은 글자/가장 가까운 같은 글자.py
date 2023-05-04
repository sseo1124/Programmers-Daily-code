
def solution(s):
    word = str()
    lst = []
    for idx, char in enumerate(s):
        if char not in word:
            lst.append(-1)
            word += char
        elif char in word:
            lst.append(idx - word.index(char))
            word = word.replace(char, ' ')
            word += char

    answer =lst
    return answer