"""
Tic Tac Toe Player
"""

import math
import copy 
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # assuming that player X always starts the game
    countO=0
    countX=0
    for y in[0,1,2]:
        for x in board[y]:
            if x=="O":
                countO=countO+1
            elif x=="X":
                countX=countX+1
    if countO>=countX:
        return X
    elif countX>countO:
        return O
        
    



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    freeboxes= set()
    for i in [0,1,2]:
        for j in [0,1,2]:
            if board[i][j]==EMPTY:
                
                freeboxes.add((i,j))
    return freeboxes


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i= action[0]
    j= action[1]
    if type(action)==list:
        action= (i,j)
    if action in actions(board): 
        if (player(board)==X):
            board[i][j]= X
        elif player(board)==O:
            board[i][j]= O
    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    """for x in [0,1,2]:
        strike=[]
        for j in [0,1,2]:
            strike.append(board[x][j])
        if ( strike[0]== strike[1]== strike[2]):
            return strike[0]"""
    if (board[0][0]== board[0][1]== board[0][2]== X or  board[1][0]== board[1][1]== board[1][2]==X or board[2][0]== board[2][1]== board[2][2]==X ):
        return X
    if (board[0][0]== board[0][1]== board[0][2]== O or  board[1][0]== board[1][1]== board[1][2]==O or board[2][0]== board[2][1]== board[2][2]==O ):
        return O
    for i in [0,1,2]:
        s2=[]
        for j in [0,1,2]:
            s2.append(board[j][i])
        if ( s2[0]== s2[1]== s2[2]):
            return s2[0]
    strikeD=[]
    for i in [0,1,2]:
        strikeD.append(board[i][i])
    if ( strikeD[0]== strikeD[1]== strikeD[2]):
        return strikeD[0]
    if( board[0][2]== board[1][1]== board[2][0]):
        return board[0][2]
    return None       




def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    Full= True
    for i in[0,1,2]:
        for j in board[i]:
            if j == None:
                Full= False
    if (Full==True ) :
        return True
    if  (winner(board) !=None):
        return True
    return False
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if (winner(board)==X):
        return 1
    elif winner(board)==O:
        return -1
    else: 
        return 0



def minimax(board):
    isMaxTurn=True if player(board)==X else False
    
    bestMove = None
    if isMaxTurn==True:
        bestScore = -math.inf
        for move in actions(board):
            result(board,move)
            score = minimax_helper(board)
            board[move[0]] [move[1]]= EMPTY
            if (score > bestScore):
                 bestScore = score
                 bestMove = move
        return bestMove
    else:
        bestScore = +math.inf
        for move in actions(board):
            result(board,move)
            score = minimax_helper(board)
            board[move[0]] [move[1]]= EMPTY
            if (score < bestScore):
                 bestScore = score
                 bestMove = move
        return bestMove



def minimax_helper( board):
    
    isMaxTurn=True if player(board)==X else False
    if terminal(board):
        return utility(board)
    scores = []
    for move in actions(board):
        result(board,move)
        scores.append(minimax_helper( board))
        board[move[0]] [move[1]]= EMPTY

    return max(scores) if isMaxTurn else min(scores)




            
            
                    
                   
                    





       

