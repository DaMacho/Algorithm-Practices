def solution(board):
    # check whether board is consist of only zeros
    _s = 0
    for i in range(len(board)):
        _s += sum(board[i][:])
    if _s == 0:
        return 0
    
    _s = 0  # initialize _s to 0
    
    table = [[x for x in sub] for sub in board]
    for x in range(1,len(table)):
        for y in range(1, len(table[x])):
            if table[x][y] == 0:
                continue
            else:
                _min = min([table[x][y-1], table[x-1][y], table[x-1][y-1]])
                table[x][y] = _min + 1
                if _s < table[x][y]:
                    _s = table[x][y]
                    
    # if board looks like identity matrix _s would be 0, but max square would be 1.
    if _s == 0:
        return 1
    else:
        return _s ** 2
