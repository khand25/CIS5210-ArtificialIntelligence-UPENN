############################################################
# CIS 521: Homework 2
############################################################

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import math
import random

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
    # two queens can attack each other if they are in the same
    # column or in the same diagonal as each other
    # given a list for the board where the index is the row
    # we have 1 queen per row guaranteed
    # so we are given a board list where the value at each index
    # is the column of the queen in that row (index)
    is_valid = True
    # handle the edge case if there is only 1 row board
    # so only 1 queen can exist
    if len(board) == 1:
        return is_valid
    # for i in range(1,len(board),1):
        # check for same column
        # queens that can
        # if board[i] == board[i-1]:
        # is_valid = False
        # return is_valid
        # check for diagonals
        # if board[i] - board[i-1] == 1:
        # is_valid = False
        # return is_valid
        # if board[i] - board[i-1] == -1:
        # is_valid = False
        # return is_valid
    # Nested for loop to iterate throough each row
    # of board where row 1 is the current row
    # and row2 will iterate internally thorugh the other
    # rows to check if same column values or same diaognal
    # values with respect to row1 or i
    for row1 in range(len(board)):
        for row2 in range(row1 + 1, len(board)):
            # check for same columns queens
            if board[row1] == board[row2]:
                is_valid = False
                return is_valid
            # check for diagonals across the entire board with
            # respect to the ith row and jth row
            if board[row1] - board[row2] == row1 - row2:
                is_valid = False
                return is_valid
            if board[row1] - board[row2] == -1 * (row1 - row2):
                is_valid = False
                return is_valid
    return is_valid


# print(n_queens_valid([0,0]))
# print(n_queens_valid([0,2]))
# print(n_queens_valid([0,1]))
# print(n_queens_valid([0,3,1]))


def n_queens_solutions(n):
    # Need to create a list containing all
    # integers from 0 to (n-1) first
    # list_of_cols = [i for i in range(0,n,1)]
    # use random function from sort randomly
    # list of possible columns and check if they
    # pass valid board from function defined above
    # number_of_sols = 0
    # result_list = []
    # while number_of_sols < n:
    #   possible_sol = random.sample(list_of_cols,k=len(list_of_cols))
    #   if n_queens_valid(possible_sol):
    #   result_list.append(possible_sol)
    #   number_of_sols += 1
    # return result_list

    # Caller the helper function and store list of solutions
    # in a 2d list called result_list
    result_list = n_queens_helper(n, [])
    return result_list


def n_queens_helper(n, board):
    # Special edge case that handles if there is
    # exactly 1 queen per row
    if len(board) == n:
        result = []
        result.append(board)
        return result

    # used to store each solution board
    solutions = []
    # iterate through n number of possible queens
    for element in range(0, n, 1):
        temp = []
        temp.append(element)
        updated_board = board + temp
        # only run below code if the current board is
        # actaully valid using our previosuly defined function
        if n_queens_valid(updated_board):
            # recursively call the n_queens_helper
            # function again to simulate dfs search
            new_board = n_queens_helper(n, updated_board)
            # each element in the new_board will be row that we can apppend
            # to the solutions list
            for value in new_board:
                solutions.append(value)
    return solutions


############################################################
# Section 2: Lights Out
############################################################


class LightsOutPuzzle(object):

    def __init__(self, board):
        result_list = []
        for row in board:
            temp = []
            for element in row:
                temp.append(element)
            result_list.append(temp)
        self.board = result_list

    def get_board(self):
        # return self.board
        result_list = []
        for row in self.board:
            temp = []
            for element in row:
                temp.append(element)
            result_list.append(temp)
        return result_list

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


b = [[True, False], [False, True]]
p = LightsOutPuzzle(b)
print(p.get_board())

b = [[True, True], [True, True]]
p = LightsOutPuzzle(b)
print(p.get_board())


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
