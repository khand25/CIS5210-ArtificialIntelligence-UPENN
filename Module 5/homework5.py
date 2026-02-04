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
    result_list = []
    for i in range(0, 9, 1):
        for j in range(0, 9, 1):
            temp = (i, j)
            result_list.append(temp)
    return result_list



def sudoku_arcs():
    possible_arcs = set()
    # iterate through all the cells in the sudoku board
    for i in range(0, 9, 1):
        for j in range(0, 9, 1):
            cell1 = (i, j)

            # same column arcs, where row are different
            # from each other
            for i2 in range(0, 9, 1):
                if i != i2:
                    cell2 = (i2, j)
                    possible_arcs.add((cell1, cell2))
            # same row arcs, where column are different
            # from each other
            for j2 in range(0, 9, 1):
                if j != j2:
                    cell2 = (i, j2)
                    possible_arcs.add((cell1, cell2))
            # same block arcs so add to the set 
            block_row_start = i - (i % 3)
            block_col_start = j - (j % 3)
            for direction_row in range(0, 3, 1):
                for direction_col in range(0, 3, 1):
                    temp = block_row_start + direction_row
                    temp2 = block_col_start + direction_col
                    cell2 = (temp, temp2)
                    if cell1 != cell2:
                        possible_arcs.add((cell1, cell2))
    return list(possible_arcs)


def read_board(path):
    result_board = dict()
    # create a set of all possible digits
    possible_digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    # store all the readable lines from the file
    # as a list
    all_lines = []
    # read the file and for each line
    # cutoof the newline character and
    # add it to the all_lines list
    with open(path, 'r') as f:
        # all_lines = []
        for line in f.readlines():
            all_lines.append(line.strip())
    # iterate through a valid sudoku board
    for i in range(0, 9, 1):
        for j in range(0, 9, 1):
            # make a row,col tuple for the key
            temp = (i, j)
            if all_lines[i][j] == "*":
                # now the empty cell will contain a set of 9 digits
                # to pick from eliminate from later
                result_board[temp] = set(possible_digits)
            else:
                # otherwise the cell will contains a set of
                # only one value which is the fixed digit
                # value it had previosuly had
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


# Read board test cases:
b = read_board("homework5_sudoku/medium1.txt")
print(Sudoku(b).get_values((0, 0)))
b = read_board("homework5_sudoku/medium1.txt")
print(Sudoku(b).get_values((0, 1)))
print("Test case for sudoku cells")
print(sudoku_cells())

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
