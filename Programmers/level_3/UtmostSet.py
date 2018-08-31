def solution(n, s):
    if n > s: return [-1]
    a = [s//n]*n
    for i in range(1,s-sum(a)+1):
        a[-i] += 1
    return a