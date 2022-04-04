from icecream import ic

board = []
with open('input.txt', 'r') as fin:
    '''
    fin = [
            "v...>>.vv>",
            ".vv>>.vv..",
            ">>.>v>...v",
            ">>v>>.>.v.",
            "v>v.vv.v..",
            ">.>>..v...",
            ".vv..>.>v.",
            "v.v..>>v.v",
            "....v..v.>",
    ]
    '''
    for j, line in enumerate(fin):
        board.append([])
        for i, token in enumerate(line.strip()):
            board[j].append(token)

#TODO: implement wrapping

turns = 0
while True:
    turns+=1
    #Eastern Movers
    movers = []
    for y in range(len(board)):
        for x in range(len(board[y])):
            try:
                if board[y][x] == ">" and board[y][x+1] == '.':
                    movers.append((x,y))
            except IndexError as e:
                if board[y][x] == ">" and board[y][0] == '.':
                    movers.append((x,y))
    for x,y in movers:
        try:
            board[y][x+1] = '>'
        except IndexError:
            board[y][0] = '>'
        board[y][x] = '.'
    east_move = bool(len(movers))
    #Southern Movers
    movers = []
    for y in range(len(board)):
        for x in range(len(board[y])):
            try:
                if board[y][x] == "v" and board[y+1][x] == '.':
                    movers.append((x,y))
            except IndexError as e:
                if board[y][x] == "v" and board[0][x] == '.':
                    movers.append((x,y))

    for x,y in movers:
        try:
            board[y+1][x] = 'v'
        except IndexError:
            board[0][x] = 'v'
        board[y][x] = '.'

    south_move = bool(len(movers))
    if not east_move and not south_move:
        ic(turns)
        break
