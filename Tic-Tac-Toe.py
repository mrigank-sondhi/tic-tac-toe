#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from IPython.display import clear_output

#Functions
def display_board(board,markers):
    clear_output()
    space='     '
    print(f'Player1:{markers[0]}                            Player2:{markers[1]}\n')
    print(
          f'{space}{space}{space}|{space}{space}{space}|{space}{space}{space}\n'
          f'{space}  {board[7]}  {space}|{space}  {board[8]}  {space}|{space}  {board[9]}  {space}\n'
          f'{space}{space}{space}|{space}{space}{space}|{space}{space}{space}\n'
           '----------------------------------------------\n'
          f'{space}{space}{space}|{space}{space}{space}|{space}{space}{space}\n'
          f'{space}  {board[4]}  {space}|{space}  {board[5]}  {space}|{space}  {board[6]}  {space}\n'
          f'{space}{space}{space}|{space}{space}{space}|{space}{space}{space}\n'
           '----------------------------------------------\n'
          f'{space}{space}{space}|{space}{space}{space}|{space}{space}{space}\n'
          f'{space}  {board[1]}  {space}|{space}  {board[2]}  {space}|{space}  {board[3]}  {space}\n'
          f'{space}{space}{space}|{space}{space}{space}|{space}{space}{space}\n'
         )

def player_input():
    mydict={'X':'O','O':'X'}
    while True:
        _ = input("What marker do you want Player2?('X' OR 'O'):")
        if _=='X' or _=='O':
            p2mark=_
            p1mark=mydict[_]
            markers=[p1mark,p2mark]
            return markers
        else:
            print('Wrong value entered,try again!')
            
def place_marker(board, marker, position):
    board[position]=marker
    
def win_check(board, mark):
    for i in range(1,8):
        if board[i]==mark:
            if i==1:
                if board[1]==board[2]==board[3]==mark:
                    return True
                elif board[1]==board[4]==board[7]==mark:
                    return True
                elif board[1]==board[5]==board[9]==mark:
                    return True
                else:
                    continue
            elif i==2:
                if board[2]==board[5]==board[8]==mark:
                    return True
                else:
                    continue
            elif i==3:
                if board[3]==board[5]==board[7]==mark:
                    return True
                elif board[3]==board[6]==board[9]==mark:
                    return True
                else:
                    continue
            elif i==4 or i==7:
                if board[i]==board[i+1]==board[i+2]==mark:
                    return True
                else:
                    continue
        else:
            continue
    return False

def space_check(board, position):
    return board[position]==' '

def full_board_check(board):
    for position in range(1,10):
        if space_check(board,position):
            return False
        else:
            continue
    return True              

def player_choice(board,num):
    while True:
        position = int(input(f'Where do you want to place your marker Player{num}?(1-9)'))
        if position>9 or position<1:
            print('Wrong position entered,choose from 1-9!')
        elif space_check(board,position):
            return position
        else:
            print('This position is full choose another one.')
            
def replay():
    choice = input('Do you want to play again?(Y/N)')
    if choice=='y' or choice=='Y':
        return True
    else:
        print('Thanks for playing.')
        return False
    
#Main Driving Code
flag=1
while flag==1:
    clear_output()
    print('Welcome to Tic Tac Toe!')
    markers = player_input()
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player_switch={1:2,2:1}
    num=1
    while True:
        display_board(board,markers)
        position = player_choice(board,num)
        place_marker(board,markers[num-1],position)
        display_board(board,markers)
        if win_check(board,markers[num-1]):
            print(f'Congratulations Player{num} you have won the game!')
            if replay():
                flag=1
                break
            else:
                flag=0
                break
        elif full_board_check(board):
            print('The game is tied!')
            if replay():
                flag=1
                break
            else:
                flag=0
                break
        else:
            num=player_switch[num]     


# In[ ]:




