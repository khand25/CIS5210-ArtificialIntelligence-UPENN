############################################################
# CIS 521: Homework 3
############################################################

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import random

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
        # intialize two instance varaibles of total rows
        # and total columns below for easier code reduncy in latter
        # methods
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
                self.empty_row = store_i - 1
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
                self.empty_col = store_j - 1
                self.board[store_i][store_j] = temp
                return True
            else:
                return False

    def scramble(self, num_moves):
        # scramble the tile puzzle on each iteration
        # where we ensure to pick some random idrection value from
        # the list below and call perform move num_moves
        # times
        possible_directions = ["up", "down", "left", "right"]
        for i in range(0, num_moves, 1):
            r_value = random.choice(possible_directions)
            self.perform_move(r_value)

    def is_solved(self):
        # keep track of the ascending order of integers
        # values throughout the board
        count = 1
        for i in range(0, len(self.board), 1):
            for j in range(0, len(self.board[0]), 1):
                if i == len(self.board) - 1 and j == len(self.board[0]) - 1:
                    # return the truthiness of if the last element is 0
                    # or not
                    return self.board[i][j] == 0
                # if the current board element is not the
                # same value as count, then
                # the board is automatically invalid!
                if self.board[i][j] != count:
                    return False
                count += 1
        return True

    def copy(self):
        # since the get_board function already returns a deep copy
        # we can simply call it and return it's return value as
        # as new TilePuzzleObject
        deep_copy = self.get_board()
        return TilePuzzle(deep_copy)

    def successors(self):
        # list containing all possible valid moves
        # to perform on a puzzle object
        possible_directions = ["up", "down", "left", "right"]
        for element in possible_directions:
            # create a new puzzle object as a deep copy of the current
            # puzzle from the calling object to perform moves
            # on
            new_puzzle = self.copy()
            # verify we are to sucessfully perform a move on the board
            valid_move = new_puzzle.perform_move(element)
            if valid_move:
                # we have to use a generator to yield the direction
                # and new puzzle object as a sequence of tuples
                result_tuple = (element, new_puzzle)
                yield result_tuple

    # Required
    def find_solutions_iddfs(self):
        # Try depths of 0, 1, 2, ... and yeild all
        # the optimal shortest moves sequences to solve
        # the entire tile puzzle
        if self.is_solved():
            # if we already have an optimal solution
            # no need for depth limited search action
            yield []
            return
        # initially start at depth 0
        depth = 0
        # initial_key = self.iddfs_helper1(self)
        # path_seen = {initial_key}
        path_moves = []
        # as long as we don't find any optimal solutions
        # at a specific depth, keep increasing the depth
        while True:
            # with the help of iddfshelper2, we can find
            # all the solutions at the current depth (if any)
            temp = list(self.iddfs_helper2(depth, path_moves))
            list_of_sols = temp
            # as long as we have atleast 1 solution at the
            # current depth return it outside of this function
            # as a directional list
            if len(list_of_sols) != 0:
                for solution in list_of_sols:
                    yield solution
                return
            # no solution at the current depth
            # so increase the depth as needed
            depth += 1

    def iddfs_helper1(self, current_puzzle):
        # current_state = []
        # convert the current board from a lists of lists
        # into a tuples of tuples for constant consistency
        # and easy acess
        temp = []
        current_board = current_puzzle.get_board()
        for i in range(0, len(current_board), 1):
            tuple_value = tuple(current_board[i])
            temp.append(tuple_value)
        # convert the temp list into a tuple for keeping
        # consistent values as needed
        temp = tuple(temp)
        return temp

    def iddfs_helper2(self, limit, moves):
        # responsible for calling the depth-limited
        # search helper
        # start with a predefined list of moves
        # to the current board. Only uses a maximum
        # limit moves
        initial_key = self.iddfs_helper1(self)
        path_visited = {initial_key}
        path_moves = list(moves)
        # error checking if total number of moves
        # given is atually more than the limit
        # cannot find solutios with these constraints
        if len(path_moves) > limit:
            return

        # call our deep copy function to get a deep copy
        # of the puzzle
        initial_puzzle = self.copy()
        # validate that the possible list of moves
        # are actually possible
        for element in path_moves:
            if initial_puzzle.perform_move(element) is False:
                return
        # Remaining depth after accounting for already-taken moves
        remaining = limit - len(path_moves)

        # Seed visited with the continuation-start state too
        path_visited = {self.iddfs_helper1(initial_puzzle)}

        # Run depth-limited DFS from that state
        yield from self.depth_first_search_helper(
            initial_puzzle, remaining, path_moves, path_visited)

    def depth_first_search_helper(self, puz, remaining, path_moves, path_expl):
        # this function will be used to perfrom dfs recurisvely
        # performs depth limited search to a specific depth and
        # returns a solution

        # goal scenario if we already arrive at a solution
        # return it and end the search
        if puz.is_solved():
            temp = list(path_moves)
            yield temp
            return
        # depth cutoff from textbook psudecode
        if remaining == 0:
            return
        # Yield the sucessor puzzle and list of moves from the
        # sucessor function
        for current_move, children in puz.successors():
            ith_term = self.iddfs_helper1(children)
            # as long as we have not seen this solution
            # yet, then explore it
            if ith_term not in path_expl:
                # make sure to mark it has been explored
                # and add it to the list of possible moves
                path_expl.add(ith_term)
                path_moves.append(current_move)
                # explore deeper into the tree with - 1
                # depth in total thus limited the search space
                yield from self.depth_first_search_helper(children,
                                                          remaining - 1,
                                                          path_moves,
                                                          path_expl)
                # for backtracking purposes according

                path_moves.pop()
                path_expl.remove(ith_term)

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

# Test case for scramble and is_solved
p = TilePuzzle([[1, 2], [3, 0]])
print(p.is_solved())
p = TilePuzzle([[0, 1], [3, 2]])
print(p.is_solved())

# Test case for copy function
p = create_tile_puzzle(3, 3)
p2 = p.copy()
print(p.get_board() == p2.get_board())

p = create_tile_puzzle(3, 3)
p2 = p.copy()
p.perform_move("left")
print(p.get_board() == p2.get_board())

# Test case for sucessors function
p = create_tile_puzzle(3, 3)
for move, new_p in p.successors():
    print(move, new_p.get_board())
b = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
p = TilePuzzle(b)
for move, new_p in p.successors():
    print(move, new_p.get_board())

# Test case for iddfs problem
b = [[4, 1, 2], [0, 5, 3], [7, 8, 6]]
p = TilePuzzle(b)
solutions = p.find_solutions_iddfs()
print(next(solutions))

b = [[1, 2, 3], [4, 0, 8], [7, 6, 5]]
p = TilePuzzle(b)
print(list(p.find_solutions_iddfs()))
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
