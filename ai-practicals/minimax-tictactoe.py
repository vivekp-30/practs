import numpy as np


board=np.full((3,3),'_')
ai_mark='O'
player_mark='X'


def print_board():
    for row in board:
        print(" ".join(row))
    print()


def is_moveleft():
    return np.any(board == '_')


def evaluate():
    for row in range(3):
        if(board[row][0] == board[row][1] == board[row][2] != '_'):
            return 10 if board[row][0] == ai_mark else -10


    for col in range(3):
        if(board[0][col] == board[1][col] == board[2][col] != '_'):
            return 10 if board[col][0] == ai_mark else -10


    if(board[0][0] == board[1][1] == board[2][2] != '_'):
        return 10 if board[0][0] == ai_mark else -10


    if(board[0][2] == board[1][1] == board[2][0] != '_'):
        return 10 if board[0][2] == ai_mark else -10
    return 0


def minmax(depth,isMaximizing):
    score = evaluate()
    if score == 10: return score - depth
    if score == -10: return score + depth
    if not is_movesleft(): return 0
   
    if(isMaximizing):
        curbest=float('-inf')
        for i in range(3):
            for j in range(3):
                if(board[i][j]=='_'):
                    board[i][j]='X'
                    curbest=max(curbest,minmax(depth+1,False))
                    board[i][j]='_'
        return best
    else:
         curbest=float('inf')
         for i  in range(3):
             for j in range(3):
                 if(board[i][j]=='_'):
                     board[i][j]='O'
                     curbest=min(curbest,minmax(depth+1,True))
                     board[i][j]='_'            
         return best


def find_bestmove():
   bestval=float('-inf')
   bestmove=(-1,-1)


   for i in range(3):
       for j in range(3):
           if(board[i][j]=='_'):
               board[i][j]='X'
               curbestVal=minmax(0,False)
               board[i][j]='_'


               if(curbestVal>bestval):
                   bestmove=(i,j)
                   bestval=curbestVal
   return bestmove[0],bestmove[1]
 
while is_moveleft() and evaluate==0:
    print_board()


    print("enter a row and column number between [0,2]:")
    row,col=map(int,input()).split()
    if(board[row][col]!='_'):
        print("the cell is already taken:)")
    else:
        board[row][col]=player_mark


        ai_row,ai_col=find_bestmove()
        board[ai_row][ai_col]=ai_mark


print_board()
evaluate()
if score==10:
    print("Ai wins")
elif score==-10:
    print("Human wins")
else:
    print("Draw")
