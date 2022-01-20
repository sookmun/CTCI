def hasWon(board,player):
    #not done implementing
    for r in range(3):
        print("r",r,"c:",0)
        if board[r][0]==player:
            print(checkVertical(board,1,player,r+1,0))
            # print(checkHorizontal(board,1,player,r+1,0))
            # break


def checkVertical(board,count,player,row,coln):
    if row>=3:
        return False
    else:
        if board[row][coln]==player:
            count+=1

    if count==3:
        return True
    else:
        return checkVertical(board,count,player,row+1,coln)


def checkDiagonal():
    pass

def checkHorizontal(board,count,player,row,coln):
    if coln>=3:
        return False
    else:
        if board[row][coln]==player:
            count+=1
    if count==3:
        return True
    else:
        return checkVertical(board,count,player,row,coln+1)



if __name__ == '__main__':
    board=[["X","X","X"],
           ["X","X",""],
           ["O","","X"]]
    hasWon(board,"X")