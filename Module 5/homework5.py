############################################################
# CIS 521: Homework 5
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
# Sudoku Solver
############################################################


def sudoku_cells():
    pass


def sudoku_arcs():
    pass


def read_board(path):
    pass


class Sudoku(object):

    CELLS = sudoku_cells()
    ARCS = sudoku_arcs()

    def __init__(self, board):
        # create a new instance variable called
        # board that will be assingned to an empty dictionary
        self.board = dict()
        # iterate through the board dictionary
        # and grab the current element 
        # (row, col) -> value 
        # cell and initialize as a new key
        # value pair to self.board dict.
        # Convert value of key to always be a set member
        # for easy duplicate values avoidance later
        for element in board.items():
            self.board[element[0]] = set(element[1])
           

    def get_values(self, cell):
        pass

    def remove_inconsistent_values(self, cell1, cell2):
        pass

    def infer_ac3(self):
        pass

    def infer_improved(self):
        pass

    def infer_with_guessing(self):
        pass

############################################################
# Feedback
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
