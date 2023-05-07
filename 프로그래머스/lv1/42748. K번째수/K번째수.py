def solution(array, commands):
    answer = []
    for command in commands:
        start_idx = command[0] - 1
        end_idx = command[1]
        k_idx = command[2] - 1
        sliced_array = sorted(array[start_idx : end_idx])
        answer.append(sliced_array[k_idx])
    return answer