#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def check_draw(board):
    return all(all(row) for row in board)

def make_move(board, player):
    while True:
        try:
            row, col = map(int, input(f"Player {player}, enter your move (row col): ").split())
            if board[row][col] == "":
                board[row][col] = player
                break
            else:
                print("This cell is already taken.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column as two numbers separated by a space.")

def find_winning_move(board, player):
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = player
                if check_win(board, player):
                    board[i][j] = ""
                    return (i, j)
                board[i][j] = ""
    return None

def ai_move(board):
    # First, check if AI can win in the next move
    move = find_winning_move(board, "O")
    if move:
        board[move[0]][move[1]] = "O"
        print(f"AI placed 'O' at ({move[0]}, {move[1]})")
        return

    # Block the player's winning move
    move = find_winning_move(board, "X")
    if move:
        board[move[0]][move[1]] = "O"
        print(f"AI placed 'O' at ({move[0]}, {move[1]})")
        return

    # Otherwise, make a random move
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ""]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = "O"
        print(f"AI placed 'O' at ({row}, {col})")


def tic_tac_toe():
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        if current_player == "X":
            make_move(board, current_player)
        else:
            ai_move(board)

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

tic_tac_toe()


# In[ ]:





# In[ ]:





# In[1]:





# In[ ]:




