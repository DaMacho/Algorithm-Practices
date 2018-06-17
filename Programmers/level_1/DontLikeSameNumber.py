def solution(arr):
    tmp = []
    for i in range(len(arr)):
        if tmp[-1:] != [arr[i]]:
            tmp.append(arr[i])
    return tmp