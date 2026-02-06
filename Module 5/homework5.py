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
import queue

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
            # cells in the same 3 X 3 blocks
            # are mutiple of 3 each other
            block_row_start = i - (i % 3)
            block_col_start = j - (j % 3)
            for direction_row in range(0, 3, 1):
                for direction_col in range(0, 3, 1):
                    temp = block_row_start + direction_row
                    temp2 = block_col_start + direction_col
                    cell2 = (temp, temp2)
                    if cell1 != cell2:
                        possible_arcs.add((cell1, cell2))
    # convert the set of possible arcs to
    # a list and return it
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
        removed = False
        # if the length of cell2 for the
        # board is 1, then we know it is filled with a single
        # posistion so we can try to remove that
        # value if it exists in cell1 as well
        if len(self.board[cell2]) == 1:
            # convert the single value set to a list
            # and grab the only item from the list
            value_to_remove = list(self.board[cell2])[0]
            # if the cell2 value exists in cell1
            # remove the inconsistent value from cell1
            # and return True for removal
            if value_to_remove in self.board[cell1]:
                self.board[cell1].remove(value_to_remove)
                removed = True
        # no removal happened so return False
        return removed

    def infer_ac3(self):
        # follow the standard AC-3 algorithm from the slides
        # initialize the arcs queue with all the arcs from the
        # given sudoku board
        arcs_queue = queue.Queue()
        # enqueue all the arcs into the queue using
        # our arcs function
        for arc in Sudoku.ARCS:
            arcs_queue.put(arc)
        # create a dictionary to store all the neighbors
        # for each cell in the sudoku board
        all_neighbors = dict()
        # initialize the neighbors an empty set
        # for each cell in the sudoku board
        for element in Sudoku.CELLS:
            all_neighbors[element] = set()
        # fill the neighbors dictionary with the
        # arcs using the ARCS function we defined
        for arc in Sudoku.ARCS:
            cell1 = arc[0]
            cell2 = arc[1]
            all_neighbors[cell1].add(cell2)
        # while the arcs queue is not empty
        while not arcs_queue.empty():
            # dequeue the current arc from the queue
            current_arc = arcs_queue.get()
            cell1 = current_arc[0]
            cell2 = current_arc[1]
            # try to remove inconsistent values
            # according to the AC-3 alogrithm
            removed = self.remove_inconsistent_values(cell1, cell2)
            if removed:
                # if the domain of cell1 is empty
                # then return failure
                if len(self.board[cell1]) == 0:
                    return False
                # otherwise for each neighbor of cell1
                # add the arc to the queue according to
                # the AC-3 algorithm
                for current_neighbor in all_neighbors[cell1]:
                    if current_neighbor != cell2:
                        arcs_queue.put((current_neighbor, cell1))
        # if we finish processing all the arcs
        # and queue gets empty, return sucess
        return True
  
    def infer_improved(self):
        # if we cannot use the AC3 inference
        # algorithm, then immeditely return failure
        if not self.infer_ac3():
            return False
        # used to store all the possible units for each cell
        # determine the possible deductons to make for each cell
        # later on and use that to make inferences and reduce the overall
        # search space
        possible_cell_units = []

        # iterate through the rows in row major order and
        # add the row units (tuples of cells in the same row) 
        # to the possible cell units list
        for i in range(0, 9, 1):
            row_units = []
            for j in range(0, 9, 1):
                row_units.append((i, j))
            possible_cell_units.append(row_units)
        
        # columns units
        # iterate through the columns in column major order and
        # add the col units (tuples of cells in the same column) 
        # to the possible cell units list
        for i in range(0, 9, 1):
            col_units = []
            for j in range(0, 9, 1):
                col_units.append((j, i))
            possible_cell_units.append(col_units)
        
        # block units
        # iterate through each of the 3 X 3 blocks
        # and add the block units (tuples of cells in the same block)
        for block_row in range(0, 9, 3):
            for block_col in range(0, 9, 3):
                block_units = []
                for direction_row in range(0, 3, 1):
                    for direction_col in range(0, 3, 1):
                        temp = (block_row + direction_row,
                                block_col + direction_col)
                        block_units.append(temp)
                possible_cell_units.append(block_units)
        # rerun AC3 algorithm continusoly until no more deductions
        # can be made
        while True:
            # if we cannot use the AC3 inference
            # algorithm, then immeditely return failure
            if not self.infer_ac3():
                return False
            # hidden singles deduction
            # for each unit in the possible cell units
            worked = False
            # for each possible value from 1 to 9
            # create a mapping of possible posistions
            # of keys 1-9
            for value in possible_cell_units:
                possible_posistions = dict()
                for i in range(1, 10, 1):
                    possible_posistions[i] = []
                # populate the possible posistions
                # mapping of keys with the cell values
                for cell in value:
                    for element in self.board[cell]:
                        possible_posistions[element].append(cell)
            
                # if any value has only one posistion so far
                # force it and assign the new posistion
                # this improves the AC3 algorithm by
                # making more deductions
                for i in range(1, 10, 1):
                    if len(possible_posistions[i]) == 1:
                        one_cell = possible_posistions[i][0]
                        temp = {i}
                        if self.board[one_cell] != temp:
                            self.board[one_cell] = temp
                            worked = True
            # if no more new assignments can be made, 
            # that means the worked boolean was not set to True
            # then
            # break the loop as the improved AC3 is done
            if not worked:
                break
        # At this point we were able to improve our
        # sudoku board so return True
        return True
            

    def infer_with_guessing(self):
        # call the previous inference function to reduce
        # the search space
        if not self.infer_improved():
            return False
        # if the board is already solved, and the assingment
        # is complete according to the backtracking algorithm,
        # then return True
        is_complete = True
        for cell_value in Sudoku.CELLS:
            if len(self.board[cell_value]) != 1:
                is_complete = False
                break
        if is_complete:
            return is_complete
        # select an unassigned variable (cell)
        # Use the minimum remainin values heuristic to select the cell
        # that has the fewest possible values to pick from
        # and leads to a good guess
        picked_cell = 0
        # have a variable store the size of the biggest
        # domain size possible
        picked_size = 20
        for cell_value in Sudoku.CELLS:
            

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
print("Test case for sudoku arcs")
print(((0, 0), (0, 8)) in sudoku_arcs())
print(((0, 0), (8, 0)) in sudoku_arcs())
print(((0, 8), (0, 0)) in sudoku_arcs())
print(((0, 0), (2, 1)) in sudoku_arcs())
print(((2, 2), (0, 0)) in sudoku_arcs())
print(((2, 3), (0, 0)) in sudoku_arcs())
print("Test case for remove inconsistent values")
sudoku = Sudoku(read_board("homework5_sudoku/easy.txt"))
print(sudoku.get_values((0, 3)))
for col in [0, 1, 4]:
    removed = sudoku.remove_inconsistent_values((0, 3), (0, col))
    print(removed, sudoku.get_values((0, 3)))
print("Test case for infer ac3")
sudoku = Sudoku(read_board("homework5_sudoku/easy.txt"))
print(sudoku.infer_ac3())
sudoku = Sudoku(read_board("homework5_sudoku/medium3.txt"))
print(sudoku.infer_improved())



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
