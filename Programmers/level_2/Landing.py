def solution(land):
    cp = [[x for x in row] for row in land]

    for r in range(1,len(land)):
        temp = cp[r-1][:]
        for i in range(len(land[0])):
            cp[r][i] = cp[r][i] + max(temp[:i] + temp[i+1:])
    return max(cp[-1])