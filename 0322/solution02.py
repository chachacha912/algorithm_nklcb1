def solution(s):
    x, y = divmod(len(s), 2)
    if (y == 0):
        answer = s[x-1:x+1]
    else:
        answer = s[x]
    return answer