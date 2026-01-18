############################################################
# CIS 521: Homework 2
############################################################

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import math
import random
import queue

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
        # Create an empty 1d list used to store the
        # 2d board
        result_list = []
        # iterate through board and for each row
        # create a temp 1d list, iterate through the current
        # row (1d list), and for each element, append it to the
        # temp list to which we later append the temp list
        # to the result_list
        # Essentially we are creating a deep copy of the board
        for row in board:
            temp = []
            for element in row:
                temp.append(element)
            result_list.append(temp)
        self.board = result_list

    def get_board(self):
        # return self.board
        # Create an empty 1d list used to store the
        # 2d board
        result_list = []
        # iterate through board and for each row
        # create a temp 1d list, iterate through the current
        # row (1d list), and for each element, append it to the
        # temp list to which we later append the temp list
        # to the result_list
        # Essentially we are creating a deep copy of the board
        for row in self.board:
            temp = []
            for element in row:
                temp.append(element)
            result_list.append(temp)
        return result_list

    def perform_move(self, row, col):
        # Toggled the light on for
        # the current posistion
        self.board[row][col] = not self.board[row][col]
        # Toggle light to opposite value for left neigbor
        # based on what light was switched on or off for the
        # given value
        if col - 1 >= 0:
            self.board[row][col - 1] = not self.board[row][col - 1]
        if col + 1 < len(self.board[0]):
            self.board[row][col + 1] = not self.board[row][col + 1]
        if row - 1 >= 0:
            self.board[row - 1][col] = not self.board[row - 1][col]
        if row + 1 < len(self.board):
            self.board[row + 1][col] = not self.board[row + 1][col]

    def scramble(self):
        for i in range(0, len(self.board), 1):
            for j in range(0, len(self.board[i]), 1):
                if random.random() < 0.5:
                    self.perform_move(i, j)

    def is_solved(self):
        for i in range(0, len(self.board), 1):
            for j in range(0, len(self.board[i]), 1):
                if self.board[i][j] is True:
                    return False
        return True

    def copy(self):
        result_board = []
        # iterate through current board
        # and manually copy over all
        # elements into result_board
        for i in range(0, len(self.board), 1):
            temp = []
            for j in range(0, len(self.board[i]), 1):
                temp.append(self.board[i][j])
            result_board.append(temp)
        return LightsOutPuzzle(result_board)

    def successors(self):
        # create a result list used to store
        # the corrdinate puzzle pairs
        result_list = []
        # Iterate through the current
        # board
        for i in range(0, len(self.board), 1):
            for j in range(0, len(self.board[i]), 1):
                # call our previous deep copy function
                # to create a new puzzle object in memory
                # contining exact same board as the current
                # instance variable
                updated_puzzle = self.copy()
                # Call the move function from above
                # to generate the sucessor puzzle
                # on the same puzzle object
                updated_puzzle.perform_move(i, j)
                row_col = (i, j)
                # generate coordinate puzzle pair
                new_element = (row_col, updated_puzzle)
                # append value to the result list as
                # a pair of coordinate puzzle
                result_list.append(new_element)
        return result_list

    def tuple_board_helper(self, board):
        # This helper function will convert the current
        # board into a tuples of tuples to more
        # easily itneract with puzzle pieces and the queue
        # function
        result = []
        for row in board:
            result.append(tuple(row))
        return tuple(result)

    # Retrieved queue module information from:
    # https://www.geeksforgeeks.org/python/queue-in-python/
    def find_solution(self):
        # Retrieve a tuple version of the board
        # for limiting changes to it
        inital_state = self.tuple_board_helper(self.board)
        # if the current board is already a solution
        # determined by our previous solved function,
        # then return an empty list to indicate
        # no additonal solution to be found
        if self.is_solved():
            return []
        # create a FIFO queue to store the frontier of states
        frontier_queue = queue.Queue()
        # Add the Updated board to the
        # frontier queue
        frontier_queue.put(inital_state)
        values_in_front = {inital_state}
        # set to limit duplicates visited states
        visited_states = set()

        parent_state = {inital_state: (None, None)}
        # BFS iteration of the board
        while not frontier_queue.empty():
            # retreive the current board from the FIFO
            # queue
            current_state = frontier_queue.get()
            # remove the current state from the dictionary
            # as it already been explored
            values_in_front.remove(current_state)
            # current state should not have been already visited.
            # if already visited, then either we have no solution or already
            # found a solution
            if current_state not in visited_states:
                visited_states.add(current_state)
                # create a new LightsOutPuzzle as the current board
                # could be a solution
                current_board = []
                for element in current_state:
                    # make the current element
                    # a list
                    temp = list(element)
                    current_board.append(temp)
                current_puzzle = LightsOutPuzzle(current_board)
                # Check to see if the new puzzle is actually a solution
                if current_puzzle.is_solved():
                    valid_moves = []
                    state = current_state
                    # as long as the parent state, was not empty
                    # lets try to add the current move to the dictionary
                    while parent_state[state][0] is not None:
                        previous_state = parent_state[state][0]
                        valid_move = parent_state[state][1]
                        valid_moves.append(valid_move)
                        state = previous_state
                    valid_moves.reverse()
                    return valid_moves
                # grab the sucessors solutions from our sucessors function
                # above and recontinue BFS iteration for them
                for move, new_p in current_puzzle.successors():
                    new_state = self.tuple_board_helper(new_p.board)

                    if new_state not in visited_states:
                        if new_state not in values_in_front:
                            parent_state[new_state] = (current_state, move)
                            frontier_queue.put(new_state)
                            values_in_front.add(new_state)
        return None


b = [[True, False], [False, True]]
p = LightsOutPuzzle(b)
print(p.get_board())

b = [[True, True], [True, True]]
p = LightsOutPuzzle(b)
print(p.get_board())


def create_puzzle(rows, cols):
    result_list = []
    for i in range(0, rows, 1):
        temp = []
        for j in range(0, cols, 1):
            temp.append(False)
        result_list.append(temp)
    return LightsOutPuzzle(result_list)


p = create_puzzle(2, 2)
print(p.get_board())
p = create_puzzle(2, 3)
print(p.get_board())

p = create_puzzle(3, 3)
p.perform_move(1, 1)
print(p.get_board())

p = create_puzzle(3, 3)
p.perform_move(0, 0)
print(p.get_board())

# Test case for is_solved function
b = [[True, False], [False, True]]
p = LightsOutPuzzle(b)
print(p.is_solved())

b = [[False, False], [False, False]]
p = LightsOutPuzzle(b)
print(p.is_solved())

# Test case for copy function
p = create_puzzle(3, 3)
p2 = p.copy()
print(p.get_board() == p2.get_board())
p = create_puzzle(3, 3)
p2 = p.copy()
p.perform_move(1, 1)
print(p.get_board() == p2.get_board())

# Test case for successor function
for i in range(2, 6):
    p = create_puzzle(i, i + 1)
    print(len(list(p.successors())))

# Test case for find_solution
p = create_puzzle(2, 3)
for row in range(2):
    for col in range(3):
        p.perform_move(row, col)
print(p.find_solution())

b = [[False, False, False], [False, False, False]]
b[0][0] = True
p = LightsOutPuzzle(b)
print(p.find_solution() is None)

############################################################
# Section 3: Linear Disk Movement
############################################################

# Retrieved BFS information/example from:
# https://www.geeksforgeeks.org/dsa/breadth-first-search-or-bfs-for-a-graph/
def solve_identical_disks(length, n):
    # edge case if no disks are given to
    # the function
    if n <= 0:
        return []
    # edge case if total number of
    # disks are mre than the total number of
    # tiles present
    if n > length:
        return None
    
    temp = []
    for i in range(0, n, 1):
        temp.append(i)
    # intial state will include all the
    # disks as a tuple
    intial_state = tuple(temp)

    temp = []
    for i in range(length - n, length, 1):
        temp.append(i)
    goal_state = tuple(temp)

    # if the disks are not needed to be
    # moved further, then no need of solutions
    # as the problem is already solved
    if intial_state == goal_state:
        return []

    frontier_queue = queue.Queue()
    frontier_queue.put(intial_state)

    values_in_front = {intial_state}
    # set to limited duplicates visited states
    visited_states = set()
    parent_state = {intial_state: (None, None)}

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
