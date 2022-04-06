import random

def player1_input(board):
    p1=input("Player 1 Enter position to play")
    if len(p1)!=2:
        print("Please Enter valid place")
        player1_input(board)
    else:
        row=int(p1[0])-1
        col=int(p1[1])-1
        if row>2 or col>2  or row<0 or col<0:
            print("Please Enter valid place")
            player1_input(board)
        else:
            if board[row][col]=="X":
                board[row][col]="+"
            else:
                print("Place is already occupied")
                player1_input(board)
    return board

def player2_input(board):
    row=random.randrange(0,3)
    col=random.randrange(0,3)
    if board[row][col]=="X":
        board[row][col]="O"
    else:
        player2_input(board)

    return board

def print_board(board):
    for i in board:
        print(i)

def get_input(play_board,n):
    if n==8:
        play_board=player1_input(play_board)
        a=check_win(play_board)
        if a==True:
            return
        else:
            print("Draw")
    else:
        play_board=player1_input(play_board)
        a=check_win(play_board)
        if a==True:
            return
        else:
            print("Computer")
            play_board=player2_input(play_board)
            b=check_win(play_board)
            if b==True:
                return
            else:
                get_input(play_board,n+2)

def check_win(play_board):

    print_board(play_board)

    if play_board[0][0]==play_board[0][1] and play_board[0][0]==play_board[0][2]:
        if play_board[0][0]!="X":
            if play_board[0][0]=="+":
                print("P1 Wins")
            else:
                print("Computer Wins")
            return True
    elif play_board[1][0]==play_board[1][1] and play_board[1][0]==play_board[1][2]:
        if play_board[1][0]!="X":
            if play_board[1][0]=="+":
                print("P1 Wins")
            else:
                print("Computer Wins")
            return True
    elif play_board[2][0]== play_board[2][1] and play_board[2][0]==play_board[2][2]:
        if play_board[2][0]!="X":
            if play_board[2][0]=="+":
                print("P1 Wins")
            else:
                print("Computer Wins")
            return True
    elif play_board[0][0]==play_board[1][0]and play_board[0][0]==play_board[2][0]:
        if play_board[0][0]!="X":
            if play_board[0][0]=="+":
                print("P1 Wins")
            else:
                print("Computer Wins")
            return True
    elif play_board[0][1]==play_board[1][1] and play_board[0][1]==play_board[2][1]:
        if play_board[0][1]!="X":
            if play_board[0][1]=="+":
                print("P1 Wins")
            else:
                print("Computer Wins")
            return True
    elif play_board[0][2]==play_board[1][2] and play_board[0][2]==play_board[2][2]:
        if play_board[0][2]!="X":
            if play_board[0][2]=="+":
                print("P1 Wins")
            else:
                print("Computer Wins")
            return True
    elif play_board[0][0]==play_board[1][1] and play_board[0][0]==play_board[2][2]:
        if play_board[0][0]!="X":
            if play_board[0][0]=="+":
                print("P1 Wins")
            else:
                print("Computer Wins")
            return True
    elif play_board[0][2]==play_board[1][1] and play_board[0][2]==play_board[2][0]:
        if play_board[0][2]!="X":
            if play_board[0][2]=="+":
                print("P1 Wins")
            else:
                print("Computer Wins")
            return True
    else:
        return False
    
print("Player 1 symbol is +")
print("Player 2 symbol is O")

board=[["X","X","X"],["X","X","X"],["X","X","X"]]

print_board(board)

print("Please enter position in row and column format")
print("Example 11 or 21 or 32")

get_input(board,0)

