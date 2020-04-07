import os

# Intilize a list for the board with empty strings
# Note: we create a list with 10 slots, but we discard the first slot so we have a 9 slots board
board = [' ' for _ in range(10)]

def insert_letter(letter, pos):
    """
    Function in charge to assign the letter X or O to its right position on the board.
    """
    board[int(pos)] = letter

def is_space_free(pos):
    """
    Function that checks if a position of the board is empty or used.
    """
    return board[int(pos)] == ' '

def is_board_full(board):
    """
    Function that checks if the the board positions are empty of full.
    """
    return not board.count(' ') > 1

def winner_check(board, letter):
    """
    Function that checks if the given letter has completed a line.
    """
    return (
        # Horizontal check
        (board[1] == letter and board[2] == letter and board[3] == letter) or
        (board[4] == letter and board[5] == letter and board[6] == letter) or
        (board[7] == letter and board[8] == letter and board[9] == letter) or
        # Vertical check
        (board[1] == letter and board[4] == letter and board[7] == letter) or
        (board[2] == letter and board[5] == letter and board[8] == letter) or
        (board[3] == letter and board[6] == letter and board[9] == letter) or
        # Diagonal
        (board[1] == letter and board[5] == letter and board[9] == letter) or
        (board[3] == letter and board[5] == letter and board[7] == letter)
    )

def draw_board(board):
    """
    Function that draw the board acording to user input.
    """
    return f"""
       |   |   
     {board[1]} | {board[2]} | {board[3]} 
       |   |   
    -----------
       |   |   
     {board[4]} | {board[5]} | {board[6]} 
       |   |   
    -----------
       |   |   
     {board[7]} | {board[8]} | {board[9]} 
       |   |   
    """

def player_move():
    """
    Function that checks wheter the player made a good move or not.
    """
    while True:
        try:
            position = input("Select a position to place an 'X' (1-9): ")
            if int(position) >= 1 and int(position) <= 9:
                if is_space_free(position):
                    insert_letter('X', position)
                    # If the letter is succesfully inserted
                    # Exit the player move function so the machine
                    break
                else:
                    print('Oops, this space is already ocupied.')
            else:
                raise ValueError
        except ValueError:
            print('Make sure you entered a valid number between 1 to 9')

def select_random(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

def computer_move():
    """
    
    """
    possible_moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = let
            if winner_check(board_copy, let):
                move = i
                return move
    
    corners_open = list()
    for i in possible_moves:
        if i in [1, 3, 7, 9]:
            corners_open.append(i)
    
    if len(corners_open) > 0:
        move = select_random(corners_open)
        return move
    
    if 5 in possible_moves:
        move = 5
        return move
    
    edges_open = list()
    for i in possible_moves:
        if i in [2, 4, 6, 8]:
            edges_open.append(i)
    
    if len(edges_open) > 0:
        move = select_random(edges_open)
        return move
    
    return move


def main():
    os.system('clear')
    print('Welcome to the Tic Tac Toe game.')
    print(draw_board(board))

    while not is_board_full(board):
        # Checking for the computer
        if not winner_check(board, 'O'):
            player_move()
            print(draw_board(board))
        else:
            os.system('clear')
            print(draw_board(board))
            print('Sorry, you lose.')
            break
        
        # Checking for the player
        if not winner_check(board, 'X'):
            position = computer_move()
            if position == 0:
                os.system('clear')
                print(draw_board(board))
                print("Tie game.")
            else:
                os.system('clear')
                insert_letter('O', position)
                print(f"Computer placed an O on position {position}.")
                print(draw_board(board))
        else:
            os.system('clear')
            print(draw_board(board))
            print('You win!')
            break


main()
while True:
    user = input("Do you want to play again? Y/N: ")
    if user.lower() == 'y':
        board = [' ' for _ in range(10)]
        print('-----------------------------------')
        main()
    else:
        break