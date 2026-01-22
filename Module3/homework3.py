############################################################
# CIS 521: Homework 3
############################################################

############################################################
# Imports
############################################################

# Include your imports here, if any are used.

############################################################

student_name = "Danyal Razaa Khan"

############################################################
# Section 1: Tile Puzzle
############################################################


def create_tile_puzzle(rows, cols):
    board = []
    max_count = rows * cols
    count = 1
    for i in range(0, rows, 1):
        temp = []
        for j in range(0, cols, 1):
            temp.append(count)
            count += 1
        board.append(temp)

    # Put 0 value in the last possible posistion of the board
    board[rows - 1][cols - 1] = 0
    return TilePuzzle(board)


class TilePuzzle(object):

    # Required
    def __init__(self, board):
        self.total_rows = len(board)
        self.total_cols = len(board[0])

        # perform a deep copy of the board to the instance
        # variable called board
        self.board = []
        for i in range(0, self.total_rows, 1):
            temp = []
            for j in range(0, self.total_cols, 1):
                temp.append(board[i][j])
            self.board.append(temp)
        # Try to locate and grab the posistion of the empty 0th tile
        # Locate the empty tile (0)
        empty_pos = None
        for r in range(self.total_rows):
            for c in range(self.total_cols):
                if self.board[r][c] == 0:
                    empty_pos = (r, c)
                    break
            if empty_pos is not None:
                break
        if empty_pos is None:
            raise ValueError("board must contain a 0 tile!")
        self.empty_row, self.empty_col = empty_pos

    def get_board(self):
        # return a deep copy of the board back to the
        # where the function is being called
        result = []
        for i in range(0, self.total_rows, 1):
            temp = []
            for j in range(0, self.total_cols, 1):
                temp.append(self.board[i][j])
            result.append(temp)
        return result

    def perform_move(self, direction):
        # check to see if the user entered a correct directional
        # value

        direction = direction.lower()
        temp_bool = False
        if direction == "up" or direction == "down":
            temp_bool = True
        if temp_bool is False:
            if direction == "left" or direction == "right":
                temp_bool = True
        # No move to be performed if invalid direction is inputted
        if temp_bool is False:
            return False
        # At this point we know the entered in value direction is
        # valid
        # Let's try to perform the move now!
        store_i = self.empty_row
        store_j = self.empty_col
        if direction == "up":
            # store_i = self.empty_row
            # store_j = self.empty_col
            # for i in range(0, self.total_rows, 1):
                # for j in range(0, self.total_cols, 1):
                    # if self.board[i][j] == 0:
                        # store_i = i
                        # store_j = j
            # up value from 0 will have the same column value
            # but row -1 value
            if store_i - 1 >= 0:
                temp = self.board[store_i - 1][store_j]
                self.board[store_i - 1][store_j] = 0
                self.empty_row = store_i -1
                self.empty_col = store_j
                self.board[store_i][store_j] = temp
                return True
            else:
                return False
        
        if direction == "down":
            # store_i = self
            # store_j = 0
            # for i in range(0, self.total_rows, 1):
                # for j in range(0, self.total_cols, 1):
                    # if self.board[i][j] == 0:
                        # store_i = i
                        # store_j = j
            # down value from 0 will have the same column value
            # but row + 1 value
            if store_i + 1 < self.total_rows:
                temp = self.board[store_i + 1][store_j]
                self.board[store_i + 1][store_j] = 0
                self.empty_row = store_i + 1
                self.empty_col = store_j
                self.board[store_i][store_j] = temp
                return True
            else:
                return False
            
        if direction == "right":
            # store_i = 0
            # store_j = 0
            # for i in range(0, self.total_rows, 1):
                # for j in range(0, self.total_cols, 1):
                    # if self.board[i][j] == 0:
                        # store_i = i
                        # store_j = j
            # right value from 0 will have the same row value
            # but col + 1 value
            if store_j + 1 < self.total_cols:
                temp = self.board[store_i][store_j + 1]
                self.board[store_i][store_j + 1] = 0
                self.empty_row = store_i
                self.empty_col = store_j + 1
                self.board[store_i][store_j] = temp
                return True
            else:
                return False
        
        if direction == "left":
            # store_i = 0
            # store_j = 0
            # for i in range(0, self.total_rows, 1):
                # for j in range(0, self.total_cols, 1):
                    # if self.board[i][j] == 0:
                        # store_i = i
                        # store_j = j
            # left value from 0 will have the same row value
            # but col - 1 value
            if store_j - 1 >= 0:
                temp = self.board[store_i][store_j - 1]
                self.board[store_i][store_j - 1] = 0
                self.empty_row = store_i
                self.empty_col = store_j -1
                self.board[store_i][store_j] = temp
                return True
            else:
                return False



    def scramble(self, num_moves):
        pass

    def is_solved(self):
        pass

    def copy(self):
        pass

    def successors(self):
        pass

    # Required
    def find_solutions_iddfs(self):
        pass

    # Required
    def find_solution_a_star(self):
        pass


p = TilePuzzle([[1, 2], [3, 0]])
print(p.get_board())
p = TilePuzzle([[0, 1], [3, 2]])
print(p.get_board())

# Test case for create_tile_puzzle
p = create_tile_puzzle(3, 3)
print(p.get_board())

p = create_tile_puzzle(2, 4)
print(p.get_board())

# Test case for perform a move
p = create_tile_puzzle(3, 3)
print(p.perform_move("Up"))
print(p.get_board())

p = create_tile_puzzle(3, 3)
print(p.perform_move("down"))
print(p.get_board())


############################################################
# Section 2: Grid Navigation
############################################################


def find_path(start, goal, scene):
    pass

############################################################
# Section 3: Linear Disk Movement, Revisited
############################################################


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
