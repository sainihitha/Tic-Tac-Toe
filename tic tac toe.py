import os
import time

def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("   Tic Tac Toe\n")
    print("     |     |")
    print("  {}  |  {}  |  {}".format(board[0], board[1], board[2]))
    print("_____|_____|_____")
    print("     |     |")
    print("  {}  |  {}  |  {}".format(board[3], board[4], board[5]))
    print("_____|_____|_____")
    print("     |     |")
    print("  {}  |  {}  |  {}".format(board[6], board[7], board[8]))
    print("     |     |\n")

def get_move(player, board):
    while True:
        move = input(f"Player {player}, enter a position (1-9): ")
        try:
            move = int(move)
            if move >= 1 and move <= 9:
                if board[move-1] == ' ':
                    return move - 1
                else:
                    print("That position is already taken.")
            else:
                print("Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def check_winner(board, player):
    return ((board[0] == player and board[1] == player and board[2] == player) or
            (board[3] == player and board[4] == player and board[5] == player) or
            (board[6] == player and board[7] == player and board[8] == player) or
            (board[0] == player and board[3] == player and board[6] == player) or
            (board[1] == player and board[4] == player and board[7] == player) or
            (board[2] == player and board[5] == player and board[8] == player) or
            (board[0] == player and board[4] == player and board[8] == player) or
            (board[2] == player and board[4] == player and board[6] == player))

def check_tie(board):
    for i in range(9):
        if board[i] == ' ':
            return False
    return True

def play_game():
    board = [' ' for i in range(9)]
    player = 'X'

    while True:
        print_board(board)
        move = get_move(player, board)
        board[move] = player

        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        elif check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        if player == 'X':
            player = 'O'
        else:
            player = 'X'

        time.sleep(1)  

    play_again = input("Play again? (Y/N)").upper()
    if play_again == "Y":
        play_game()


play_game()
