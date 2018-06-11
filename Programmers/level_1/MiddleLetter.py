def solution(st):
    if len(st) > 2:
        if len(st)%2 == 0:
            return st[int(len(st)/2)-1:int(len(st)/2)+1]
        if len(st)%2 != 0:
            return st[int((len(st)-1)/2)]
    else:
        return st