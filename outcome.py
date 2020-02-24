def xWin(board):
    if ['X', 'X', 'X'] in board:
        return True
    for i in range(3):
        if board[0][i]==board[1][i]==board[2][i]=='X':
            return True
    if board[0][0]==board[1][1]==board[2][2]=='X':
        return True
    if board[0][2]==board[1][1]==board[2][0]=='X':
        return True
    return False

def oWin(board):
    if ['O', 'O', 'O'] in board:
        return True
    for i in range(3):
        if board[0][i]==board[1][i]==board[2][i]=='O':
            return True
    if board[0][0]==board[1][1]==board[2][2]=='O':
        return True
    if board[0][2]==board[1][1]==board[2][0]=='O':
        return True
    return False

def tieGame(board):
    if xWin(board):
        return False
    elif oWin(board):
        return False
    for row in board:
        if '' in row:
            return False
    return True
