############################################################
# CIS 521: Homework 2
############################################################

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import math

############################################################

student_name = "Danyal Razaa Khan"

############################################################
# Section 1: N-Queens
############################################################


def num_placements_all(n):
    # Return the number of ways to place n queens on an n x n chessboard
    # We can find this result by using the statistics formula for combinations
    # C = n! / (k! * (n-k)!)
    # where n is the total number of chess squares
    # (n*n) and k is the number of queens
    # updating the formula gives us:
    # C = (n)^2! / (n! * (n^2 - n)!)
    # where now n is k and n
    total_num_placements = math.factorial(n * n)
    temp_denominator = math.factorial((n * n) - n)
    total_denominator = math.factorial(n) * temp_denominator
    total_num_placements = total_num_placements // total_denominator
    return total_num_placements


def num_placements_one_per_row(n):
    # Trying to count the number of boards with n queens
    # such that there is exactly one queen in each row.
    # Because there is one queen in each row,
    # And n number of rows
    # And n number of columns tiles
    # The first row has n options for placing a queen
    # so the value would be n^n
    num_placements_per_row = n ** n
    return num_placements_per_row


def n_queens_valid(board):
    pass


def n_queens_solutions(n):
    pass

############################################################
# Section 2: Lights Out
############################################################


class LightsOutPuzzle(object):

    def __init__(self, board):
        pass

    def get_board(self):
        pass

    def perform_move(self, row, col):
        pass

    def scramble(self):
        pass

    def is_solved(self):
        pass

    def copy(self):
        pass

    def successors(self):
        pass

    def find_solution(self):
        pass


def create_puzzle(rows, cols):
    pass

############################################################
# Section 3: Linear Disk Movement
############################################################


def solve_identical_disks(length, n):
    pass


def solve_distinct_disks(length, n):
    pass

############################################################
# Section 4: Feedback
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
