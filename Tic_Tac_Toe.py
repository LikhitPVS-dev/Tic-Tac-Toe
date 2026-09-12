#main function that prints boards
def main():
    while True:
        print("************************************************************")
        choice=int(input('Enter the game mode you wanna play:\n1.vs friend\n2.vs ai\n:'))
        print("************************************************************")
        if choice==1:
            two_player()
            break
        elif choice==2:
            ai()
            break
        else:
            print('please choose valid choice')
    

#printing board
def display_board(board):
    c=0
    
    for i in board:
        for j in i:
            c+=1
            if j is None:
                print('|','#',c,end='|')
            else:
                print('|',j,'  ',end='|')
        print()


#function if the user selects 2 player mode
def two_player():
    try:
        print('Enter the number 1-9 to select the box(press Enter to quit)')
        board=[[None,None,None],[None,None,None],[None,None,None]]
        display_board(board)
        while (None in board[0] or None in board[1] or None in board[2]) and winner(board):
            player1=int(input('enter your choice(player 1):'))
            testing(player1,board,'⭕')
            if not(winner(board)):
                print(f"PLAYER 1 WON!!!🥳")
                break
            check_draw(board)
            player2=int(input('enter your choice(player 2):'))
            testing(player2,board,'❌')
            if not(winner(board)):
                print("PLAYER 2 WON!!!🥳")
                break
            check_draw(board)
    except ValueError:
        print('You quit the game!!')
    
        
def check_draw(board):
    if not(None in board[0] or None in board[1] or None in board[2] and winner(board)):
        print("It's a draw!")
    



def testing(player,board,sym):
    if player>9:
        print('please input a valid choice')
    else:
        if player<=0:
            print(f'{player} is invalid choice')
        elif player<=3 and board[0][player-1] is None:
            board[0][player-1]=(sym)
        elif player<=6 and player>3 and board[1][player-4] is None:
            board[1][player-4]=(sym)
        elif player<=9 and player>6 and board[2][player-7] is None:
            board[2][player-7]=(sym)
        else:
            print("************************************************")
            print('THE BOX IS ALREADY FILLED !!! TRY ANOTHER BOX')
            print("************************************************")
            player_=int(input('try entering another number:'))
            testing(player_,board,sym)
            return 0
    display_board(board)

    

#funt to play with ai
def ai():
    
    #display_board(board)
    pass


#function to declare winner or loser
def winner(board):
    
    
    d,d_=0,0
    for i in range(3):
        r,r_=0,0
        for j in range(3):
            if board[i][j]=='❌':
                r+=1
            elif board[i][j]=='⭕':
                r_+=1
        if (r==3 or r_==3):
            return False
    
    for i in range(3):
        c,c_=0,0
        for j in range(3):
            if board[j][i]=='❌':
                c+=1
            elif board[j][i]=='⭕':
                c_+=1
        if (c==3 or c_==3):
            return False

    for i in range(3):
        if board[i][i]=='❌':
            d+=1
        elif board[i][i]=='⭕':
            d_+=1
    if (d==3 or d_==3):
        return False
    d,d_=0,0
    for i in range(3):
        if board[2-i][i]=='❌':
            d+=1
        elif board[2-i][i]=='⭕':
            d_+=1
    if (d==3 or d_==3):
        return False

      
    return True
if __name__=='__main__':
    main()