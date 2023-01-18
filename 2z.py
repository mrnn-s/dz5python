
import random

# доска
board = [[' ',' ',' '],
         [' ',' ',' '],
         [' ',' ',' ']]
def print_board(board):
    for row in board:
        print(' '.join(row))

print(board )

player = 'X'
game_still_going = True
winner = None

def handle_turn(player):
    if player == 'X':
        # player turn
        print(f'{player} turn.')
        print('Enter  (0, 1, 2): ')
        row = int(input())
        print('Enter  (0, 1, 2): ')
        col = int(input())
        if board[row][col] == ' ':
            board[row][col] = player
        else:
            print('занято,еще раз.')
            handle_turn(player)
    else:
        # bot 
        row, col = bot_turn()
        board[row][col] = player


def bot_turn():
    available_cells = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                available_cells.append((row, col))
    if len(available_cells) > 0:
        return random.choice(available_cells)
    else:
        return None, None


def check_for_winner(board, player):
    for row in range(3):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    # Check columns
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False


while game_still_going:
    print_board(board)
    handle_turn(player)
    winner = check_for_winner(board, player)
    if winner:
        print(f'{player} won!')
        game_still_going = False
    if ' ' not in [cell for row in board for cell in row]:
        print("ничья!")
        game_still_going = False

    if player == 'X':
        player = 'O'
    else:
        player = 'X'
