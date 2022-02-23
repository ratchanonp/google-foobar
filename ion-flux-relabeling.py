def findParent(height, node):

    start = 1
    end = pow(2, height) - 1
    
    if (end == node):
        return -1
    
    while(node >= 1):
        end = end - 1
        mid = start + (end - start)//2

        if(mid == node or end == node):
            return (end + 1)
        elif (node < mid):
            end = mid
        else:
            start = mid


def solution(h, q):
    answer = []
    for i in q:
        answer.append(findParent(h, i))

    print(*answer, sep=',')
    
solution(3, [7, 3, 5, 1])
solution(5, [19, 14, 28])