def solution(nums):
    # 뽑을 수 있는 포켓몬 마리수
    pick = len(nums) / 2
    # 주어진 폰켓몬중에 중복된 폰켓몬 제외
    nums = list(set(nums))
    if len(nums) < pick:
        answer = len(nums)
    else:
        answer = pick
    return answer