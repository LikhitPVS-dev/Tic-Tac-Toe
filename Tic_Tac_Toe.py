#imports
import random
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
            while True:
                choise=int(input("choose your difficuly\n1.easy\n2.medium\n3.hard\n:"))
                if choise==1:
                    easy_ai()
                    break
                elif choise==2:
                    med_ai()
                    break
                elif choise==3:
                    hard_ai()
                    break
                else:
                    print('please enter valid input')
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
                print('|',j,end='|')
        print()
#function if the user selects 2 player mode
def two_player():
    try:
        print('Enter the number 1-9 to select the box(press Enter to quit)')
        board=[[None,None,None],[None,None,None],[None,None,None]]
        display_board(board)
        while not (check_draw_winner(board)):
            player1=int(input('enter your choice(player 1):'))
            testing(player1,board,'⭕',2)
            if not(winner(board,'⭕')):
                print(f"PLAYER 1 WON!!!🥳")
                break
            if check_draw_winner(board):
                print("It\'s a draw!!!")
                break
            
            player2=int(input('enter your choice(player 2):'))
            testing(player2,board,'❌',2)
            if not(winner(board,'❌')):
                print("PLAYER 2 WON!!!🥳")
                break
            if check_draw_winner(board):
                print("It\'s a draw!!!")
    except ValueError:
        print('You quit the game!!')   
def check_draw_winner(board):
    if not((None in board[0] or None in board[1] or None in board[2]) and (winner(board,'❌') or winner(board,'⭕'))):
        return True
    return False
def testing(player,board,sym,play):
    if player>9:
        print('please input a valid choice')
        if play==1:
            return False
    else:
        if player<=0:
            print(f'{player} is invalid choice')
            if play==1:
                return False
        elif player<=3 and board[0][player-1] is None:
            board[0][player-1]=(sym)
            if play==1:
                return True
        elif player<=6 and player>3 and board[1][player-4] is None:
            board[1][player-4]=(sym)
            if play==1:
                return True
        elif player<=9 and player>6 and board[2][player-7] is None:
            board[2][player-7]=(sym)
            if play==1:
                return True
        else:
            if play==2:
                print("************************************************")
                print('THE BOX IS ALREADY FILLED !!! TRY ANOTHER BOX')
                print("************************************************")
                player_=int(input('try entering another number:'))
                display_board(board)
                testing(player_,board,sym,2)
            else:
                return False

    if play==2:        
        display_board(board)
    
def winning_move(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                board[i][j]='⭕'
                if not(winner(board,'⭕')): 
                    return True
                else:
                    board[i][j]=None
    return False
    
def blocking_move(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                board[i][j]='❌'
                if not(winner(board,'❌')):
                    board[i][j]='⭕'
                    return True
                else:
                    board[i][j]=None
    return False
def random_move(board):
    var=random.randint(1,9)
    while(not(testing(var,board,'⭕',1))):
        var=random.randint(1,9)
    return var
def easy_ai():
    try:
        board=[[None,None,None],[None,None,None],[None,None,None]]
        display_board(board)
        while not(check_draw_winner(board)):
            print('ai is making it\'s move....')
            var=random_move(board)
            display_board(board)
            if not winner(board,'⭕'):
                print("ai won!")
                break
            elif check_draw_winner(board):
                print("It\'s a draw!!!")
                break
            player=int(input('Enter your move:'))
            testing(player,board,'❌',2)
            if not winner(board,'❌'):
                print("you won!")
                break
            elif check_draw_winner(board):
                print("It\'s a draw!!!")
                break
    except ValueError:
        print('You quit the game!!')
def med_ai():
    try:
        board=[[None,None,None],[None,None,None],[None,None,None]]
        display_board(board)
        while not(check_draw_winner(board)):
            print('ai is making\'s move....')
            if winning_move(board):
                display_board(board)
            elif blocking_move(board):
                display_board(board)
            else:
                random_move(board)
                display_board(board)
            if not(winner(board,'⭕')):
                print('ai won')
                break
            elif check_draw_winner(board):
                print("It\'s a draw!!!")
                break
            player=int(input('Enter your move:'))
            testing(player,board,'❌',2)
            if not winner(board,'❌'):
                print("you won!")
                break
            elif check_draw_winner(board):
                print("It\'s a draw!!!")
                break
    except ValueError:
        print('You quit the game!!')
def minimax_ai(board,ai_turn):
    if not(winner(board,'⭕')):
        return 10
    elif not(winner(board,'❌')):
        return -10
    elif check_draw_winner(board):
        return 0
    ls=[]
    c=0
    for i in range(3):
        for j in range(3):
            c+=1
            if board[i][j] is None:
                ls.append(c)
    scores=[]
    
    for i in ls:
        new_board=[board[0].copy(),board[1].copy(),board[2].copy()]
        if ai_turn:
            testing(i,new_board,'⭕',1)
        else:
            testing(i,new_board,'❌',1)
        scores.append(minimax_ai(new_board,not(ai_turn)))
    if ai_turn:
        return max(scores)
    else:
        return min(scores)





def hard_ai():
    try:
        board=[[None,None,None],[None,None,None],[None,None,None]]
        display_board(board)
        while not(check_draw_winner(board)):
            print('ai is making\'s move....')
            scores=[]
            c=0
            ls=[]
            for i in range(3):
                for j in range(3):
                    c+=1
                    if board[i][j] is None:
                        ls.append(c)
            for move in ls:
                new_board=[board[0].copy(),board[1].copy(),board[2].copy()]
                testing(move,new_board,'⭕',1)
                score=minimax_ai(new_board,False)
                scores.append(score)
            best_move = ls[scores.index(max(scores))]
            testing(best_move, board, '⭕', 1)
            display_board(board)
            if not(winner(board,'⭕')):
                print('ai won')
                break
            elif check_draw_winner(board):
                print("It\'s a draw!!!")
                break
            player=int(input('Enter your move:'))
            testing(player,board,'❌',2)
            if not winner(board,'❌'):
                print("you won!")
                break
            elif check_draw_winner(board):
                print("It\'s a draw!!!")
                break
    except ValueError:
        print('You quit the game!!')


#function to declare winner or loser
def winner(board,sym):
    d=0
    for i in range(3):
        r=0
        for j in range(3):
            if board[i][j]==sym:
                r+=1
        if (r==3):
            return False
    
    for i in range(3):
        c=0
        for j in range(3):
            if board[j][i]==sym:
                c+=1
        if (c==3 ):
            return False

    for i in range(3):
        if board[i][i]==sym:
            d+=1
    if (d==3):
        return False
    d=0
    for i in range(3):
        if board[2-i][i]==sym:
            d+=1
    if (d==3):
        return False
    return True
if __name__=='__main__':
    main()