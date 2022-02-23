def solution(l ,t):
    length = len(l)
    shortest_start, shortest_end = -1, -1
    
    for start in range(length):
        for end in range(start, length + 1):
            if sum(l[start:end]) == t:
                if start < shortest_start or shortest_start == -1:
                    shortest_start = start
                    shortest_end = end - 1
    
    return [shortest_start, shortest_end]

print(solution([4, 3, 5, 7, 8], 12))