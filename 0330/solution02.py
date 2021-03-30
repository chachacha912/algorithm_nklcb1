def solution(citations):
    citations.sort()
    ci_len = len(citations)
    while True :
        for i, value in enumerate(citations):
            if value >= ci_len and len(citations[i:]) >= ci_len :
                return ci_len
        else :
            ci_len -= 1
            continue
        break


print(solution([3, 0, 6, 1, 5]))
