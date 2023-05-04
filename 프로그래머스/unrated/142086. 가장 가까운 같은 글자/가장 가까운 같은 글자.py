
def solution(s):
    word = str()
    ls = []
    for idx, char in enumerate(s):
        if char not in word:
            ls.append(-1)
            word += char
        elif char in word:
            ls.append(idx - word.index(char))
            word = word.replace(char, ' ')
            word += char

    answer =ls
    return answer