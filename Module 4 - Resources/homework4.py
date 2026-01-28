############################################################
# CIS 521: Homework 4
############################################################

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import collections
import copy
import itertools
import random
import math

############################################################

student_name = "Danyal Razaa Khan"

############################################################
# Section 1: Dominoes Game
############################################################


class DominoesGame(object):

    # Required
    def __init__(self, board):
        # create an instance variable called board,
        # used to store the board's reference in memory
        self.board = board
        self.total_rows = len(self.board)
        self.total_cols = len(self.board[0])

    def get_board(self):
        # return a shallow copy of the board
        return self.board

    def reset(self):
        for i in range(0, self.total_rows, 1):
            for j in range(0, self.total_cols, 1):
                # if we currently have a True value
                # in the current ith,jth posistion
                # then set it to False
                self.board[i][j] = False

    def is_legal_move(self, row, col, vertical):
        # check to see if either row or col
        # is valid indicies in the board
        if row < 0 or col < 0:
            return False
        if row >= self.total_rows or col >= self.total_cols:
            return False
        
        valid = False
        # if we are dealing with a vertical move
        if vertical:
            # if the row below is actaully in bounds
            if row + 1 < self.total_rows:
                if self.board[row][col] is False:
                    if self.board[row + 1][col] is False:
                        valid = True
        else:
            # we are dealing with a horizontal move
            if col + 1 < self.total_cols:
                # if the col to the right is actaully in bounds
                if self.board[row][col] is False:
                    if self.board[row][col + 1] is False:
                        valid = True
        return valid


    def legal_moves(self, vertical):
        pass

    def perform_move(self, row, col, vertical):
        pass

    def game_over(self, vertical):
        pass

    def copy(self):
        pass

    def successors(self, vertical):
        pass

    def get_random_move(self, vertical):
        pass

    # Required
    def get_best_move(self, vertical, limit):
        pass


# Test case for get_board()
b = [[False, False], [False, False]]
g = DominoesGame(b)
print(g.get_board())

b = [[True, False], [True, False]]
g = DominoesGame(b)
print(g.get_board())

# Test case for reset
b = [[False, False], [False, False]]
g = DominoesGame(b)
print("Test case for reset")
print(g.get_board())
g.reset()
print(g.get_board())
b = [[True, False], [True, False]]
g = DominoesGame(b)
print(g.get_board())
g.reset()
print(g.get_board())
print("Test case for is_legal_move")
b = [[False, False], [False, False]]
g = DominoesGame(b)
print(g.is_legal_move(0, 0, True))
print(g.is_legal_move(0, 0, False))
b = [[True, False], [True, False]]
g = DominoesGame(b)
print(g.is_legal_move(0, 0, False))
print(g.is_legal_move(0, 1, True))
print(g.is_legal_move(1, 1, True))


def create_dominoes_game(rows, cols):
    # create a 2d list of all False boolean
    # values with the same dimensions of the
    # dominoes board given
    empty_board = []
    for i in range(0, rows, 1):
        temp = []
        for j in range(0, cols, 1):
            temp.append(False)
        empty_board.append(temp)
    # create a new dominoes object with the empty_board
    # passed in via the constructor for this object
    return DominoesGame(empty_board)


# Test case for create_dominoes_game function:
print("Test case for create_dominoes_game")
g = create_dominoes_game(2, 2)
print(g.get_board())

g = create_dominoes_game(2, 3)
print(g.get_board())
############################################################
# Section 2: Feedback
############################################################


# Just an approximation is fine.
feedback_question_1 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_2 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_3 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""
