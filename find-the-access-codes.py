from itertools import combinations


def solution(l):
    l = sorted(l)
    sol = [[x, y, z] for x, y, z in combinations(l, 3) if z % y == 0 and y % x == 0]
    return sol


print(solution([1, 1, 1, 2]))
