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
            # and both sqaures are currently empty
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
        # we are dealing with a vertical moving dominoe
        # player
        if vertical:
            # iterate through all the rows and columns of the
            # instance variable board for the calling object 
            # on each iteration, call our is_legal_move
            # function from above to indicate where our current row
            # and column from the board iteration is able to place
            # a dominoe piece vertically on top of it.
            # if True returned, then yeild the row and col
            # as a generator tuple elment to puase this function
            # return the tuple, and recontinue this function
            # onto the next iteration of the loop
            for i in range(0, self.total_rows, 1):
                for j in range(0, self.total_cols, 1):
                    if self.is_legal_move(i, j, True):
                        yield(i, j)
        else:
            # we are dealing with a horizontal moving dominoe
            # player.
            # iterate through all the rows and columns of the
            # instance variable board for the calling object 
            # on each iteration, call our is_legal_move
            # function from above to indicate where our current row
            # and column from the board iteration is able to place
            # a dominoe piece horizontally on top of it.
            # if True returned, then yeild the row and col
            # as a generator tuple elment to pause this function
            # return the tuple, and recontinue this function
            # onto the next iteration of the loop
            for i in range(0, self.total_rows, 1):
                for j in range(0, self.total_cols, 1):
                    if self.is_legal_move(i, j, False):
                        yield(i, j)
        

    def perform_move(self, row, col, vertical):
        # we are dealing with a vertical moving dominoe
        # player
        if vertical:
            # verify if we can place the veritcal dominoe at the
            # given row col posistion
            if self.is_legal_move(row, col, True):
                self.board[row][col] = True
                self.board[row + 1][col] = True
        else:
            # verify if we can place the horizontal dominoe at the
            # given row col posistion
            if self.is_legal_move(row, col, False):
                self.board[row][col] = True
                self.board[row][col + 1] = True


    def game_over(self, vertical):
        # if the player is playing vertical dominoes
        if vertical:
            # iterate through all the rows and columns of the
            # the board, perform wheter the current row and col
            # is legal, if so the game is not complete as a move
            # can be made so no game over
            for i in range(0, self.total_rows, 1):
                for j in range(0, self.total_cols, 1):
                    if self.is_legal_move(i, j, True):
                        return False
        else:
            # if the player is playing horizontal dominoes
            # iterate through all the rows and columns of the
            # the board, perform wheter the current row and col
            # is legal, if so the game is not complete as a move
            # can be made so no game over
            for i in range(0, self.total_rows, 1):
                for j in range(0, self.total_cols, 1):
                    if self.is_legal_move(i, j, False):
                        return False
        return True

    def copy(self):
        result = []
        for i in range(0, self.total_rows, 1):
            temp = []
            for j in range(0, self.total_cols, 1):
                temp.append(self.board[i][j])
            result.append(temp)
        return DominoesGame(result)
                
    
    def successors(self, vertical):
        if vertical:
            for i in range(0, self.total_rows, 1):
                for j in range(0, self.total_cols, 1):
                    if self.is_legal_move(i, j, True):
                        new_game = self.copy()
                        new_game.perform_move(i, j, True)
                        result_tuple = ((i, j), new_game)
                        yield result_tuple
        else:
            for i in range(0, self.total_rows, 1):
                for j in range(0, self.total_cols, 1):
                    if self.is_legal_move(i, j, False):
                        new_game = self.copy()
                        new_game.perform_move(i, j, False)
                        result_tuple = ((i, j), new_game)
                        yield result_tuple


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

# Test case for legal_moves
print("Test cases for legal_moves function")
g = create_dominoes_game(3, 3)
print(list(g.legal_moves(True)))
print(list(g.legal_moves(False)))
b = [[True, False], [True, False]]
g = DominoesGame(b)
print(list(g.legal_moves(True)))
print(list(g.legal_moves(False)))
print("Test cases for perform moves function")
g = create_dominoes_game(3, 3)
g.perform_move(0, 1, True)
print(g.get_board())
g = create_dominoes_game(3, 3)
g.perform_move(1, 0, False)
print(g.get_board())
print("Test case for game over:")
b = [[False, False], [False, False]]
g = DominoesGame(b)
print(g.game_over(True))
print(g.game_over(False))
b = [[True, False], [True, False]]
g = DominoesGame(b)
print(g.game_over(True))
print(g.game_over(False))
print("Test case for copy function:")
g = create_dominoes_game(4, 4)
g2 = g.copy()
print(g.get_board() == g2.get_board())
g = create_dominoes_game(4, 4)
g2 = g.copy()
g.perform_move(0, 0, True)
print(g.get_board() == g2.get_board())
print("Test case for sucessors function")
b = [[False, False], [False, False]]
g = DominoesGame(b)
for m, new_g in g.successors(True):
    print(m, new_g.get_board())
b = [[True, False], [True, False]]
g = DominoesGame(b)
for m, new_g in g.successors(True):
    print(m, new_g.get_board())

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
