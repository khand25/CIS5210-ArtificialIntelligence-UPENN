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
    result_board = dict()
    possible_digits = {1,2,3,4,5,6,7,8,9}
    all_lines = []
    with open(path, 'r') as f:
        # all_lines = []
        for line in f.readlines():
            all_lines.append(line.strip())
        
    for i in range(0, 9, 1):
        for j in range(0, 9, 1):
            temp = (i, j)
            if all_lines[i][j] == "*":
                # now the empty cell will contain a set of 9 digits
                # to pick from eliminate from later
                result_board[temp] = set(possible_digits)
            else:
                result_board[temp] = {int(all_lines[i][j])}
    return result_board



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
        return set(self.board[cell])

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
