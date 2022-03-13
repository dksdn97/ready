import itertools
def solution(nums):
    answer = 0
    numb = list(itertools.combinations(nums, 3))
    print(numb)
    for i in numb:
        sumnumb = sum(i)
        for j in range(2, sumnumb):
            if sumnumb % j == 0:
                break
        if j == sumnumb - 1:
            answer += 1

    return answer

nums = [ 1,2,7,6,4]
print(solution(nums))
