import itertools
def solution(numbers):
    answer = itertools.combinations(numbers, 2)
    lists= []

    for i in answer:
        lists.append(i[0]+i[1])
    a = list(set(lists))
    a.sort()
    return a
