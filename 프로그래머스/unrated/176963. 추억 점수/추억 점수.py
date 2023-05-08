def solution(name, yearning, photo):
    answer = []
    for people in photo:
        rating = []
        for friend, score in zip(name, yearning):
                if friend in people:
                    rating.append(score)
        scoring = sum(rating)
        answer.append(scoring)           
    return answer