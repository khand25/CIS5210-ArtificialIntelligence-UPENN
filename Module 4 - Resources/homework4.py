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


def create_dominoes_game(rows, cols):
    pass


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
        pass

    def is_legal_move(self, row, col, vertical):
        pass

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
