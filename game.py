import random
#from IPython.display import clear_output
#test_board = ['#', 'x', 'o', 'x', 'o', 'x', 'o', 'x', 'o', 'x']

def display_board(board):
    #clear_output()
    print(board[7] + '|' + board[8] + '|' + board[9] + '|')
    print('-|-|-')
    print(board[4] + '|' + board[5] + '|' + board[6] + '|')
    print('-|-|-')
    print(board[1] + '|' + board[2] + '|' + board[3] + '|')
def player_input():
    marker = ''
    while not (marker == 'x' or marker =='o'):
        marker = input("player 1 choose x or o ")
    if marker == 'x':
        return ('x','o')
    else:
        return ('o','x')
def win_checkboard(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[9] == mark and board[5] == mark and board[1] == mark))
    while marker != 'x' and marker != 'o':
        marker = input('player 1 choose x or o: ')
    player1 = marker

    if player1 == 'x':
        player2 = 'o'
    else:
        player2 = 'x'
    return(player1,player2)

def place_holder(board,marker,position):
    board[position] = marker

def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'player 1'
    else:
        return 'player 2'
def space_checker(board,position):
    return board[position] == ''
def full_board(board):
    for i in range(1,10):
        if space_checker(board,i):
            return False
    return True
def choice_checker(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_checker(board, position):
        position = int(input("Enter a position: (1-9) "))
    return position
def replay(board):
    choice = input("Play again? Enter Yes or No ")
    return choice == 'Yes'
print("Welcome to Tic Tac")
while True:
    test_board = [''] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first')
    play_game = input('want to play y or n: ')
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == 'player 1':
            display_board(test_board)
            position = choice_checker(test_board)
            place_holder(test_board,player1_marker,position)
            if win_checkboard(test_board,player1_marker):
                display_board(test_board)
                print("player 1 has won")
                game_on = False
            else:
                if full_board(test_board):
                    display_board(test_board)
                    print('Tie game')
                    break
                else:
                    turn = 'player 2'

        else:
            display_board(test_board)
            position = choice_checker(test_board)
            place_holder(test_board, player2_marker, position)
            if win_checkboard(test_board, player2_marker):
                display_board(test_board)
                print("player 2 has won")
                game_on = False
            else:
                if full_board(test_board):
                    display_board(test_board)
                    print('Tie game')
                    break
                else:
                    turn = 'player 1'
    if not replay(test_board):
        break
