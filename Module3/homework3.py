############################################################
# CIS 521: Homework 3
############################################################

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import random
import math
from queue import PriorityQueue

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
        # edge case to check is the
        # board is already solved, so no 
        # lists of solutions available to 
        # return
        if self.is_solved():
            temp = []
            return temp
        # have a deep copy of the currnet self puzzle called 
        # initial puzzle for not mutations to the calling
        # object's board
        initial_puzzle = self.copy()
        # use our helper form iddfs as we can reuse
        # this function to convert the board from the
        # list of lists to a tuples of tuples
        initial_key = self.iddfs_helper1(initial_puzzle)
        # priority queue data structure needed for A *
        # search algorithm
        p_queue = PriorityQueue()
        # counter used to count the total number of moves
        # requried between starting and goal coordinates
        counter = 0

        # f(n) = g(n) + h(n)
        # retrieve our h(n) value or best educated
        # guess value from the manhattan distance 
        # function
        heuristic = self.manhattan_heuristic_helper(initial_puzzle)
        # our cost from the starting origin point
        g_funct = {initial_key: 0}
        # place the current function generated distance, counter value
        # and coordinate posistion into the pq
        p_queue.put((0.0 + heuristic, counter, initial_key))
        counter += 1
        # parent pointer from the previous path
        came_from = {}
        # expand a tracked previosly pop key
        puzzle_key = {initial_key: initial_puzzle}
        # the set of node we have already accounted
        # for and explored
        done_nodes = set()
        




    def manhattan_heuristic_helper(self, tile_puzzle):
        # heurstic function for find_solution_a_star 
        # function using the manhattan distance formula
        # distance = |x1 - x2| + |y1 - y2|
        # Tile_puzzle object is refrencesing a null space
        # in memory, then use the current calling object's
        # tile puzzle
        if tile_puzzle is None:
            tile_puzzle = self
        # recieve a deep copy of the board
        # and have it refrenced by current_board
        current_board = tile_puzzle.get_board()
        total_rows = len(current_board)
        total_cols = len(current_board[0])
        # dictionary to keep track of the list of
        # tile coordinates and thier associated
        # tile number together
        posistion_goal = {}
        # now keep track of the ending coordinates
        # values with respect to the manhattan distance
        # calculation
        for i in range(1, total_rows * total_cols):
            goal_row = (i - 1) // total_cols
            goal_col = (i - 1) % total_cols
            posistion_goal[i] = (goal_row, goal_col)
        # actually manhattan distance calculation
        sum_manhattan = 0
        # iterate throgh the board, and as long as we are not on the empty tile,
        # then apply the manahattan distance forumal for every point
        # with respect to it's desitnation point
        for i in range(0, total_rows, 1):
            for j in range(0, total_cols, 1):
                # if the current board tile is not
                # the empty tile
                if current_board[i][j] != 0:
                    row_goal = posistion_goal[current_board[i][j]][0]
                    col_goal = posistion_goal[current_board[i][j]][1]
                    sum_manhattan += abs(i - row_goal)
                    sum_manhattan += abs(j - col_goal)
        return sum_manhattan








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
    # in the case we are given an empty scene
    if not scene or not scene[0]:
        return None
    # start is tuple of coordinates with
    # (row, column) for the point
    start_row = start[0]
    start_col = start[1]
    # goal is tuple of coordinates with
    # (row, column) for the point
    goal_row = goal[0]
    goal_col = goal[1]
    # dimensions of the scene to comply to
    total_rows = len(scene)
    total_cols = len(scene[0])
    # if either the start point or the end point
    # lie outside the scene, return None to indicate
    # no solution exists
    if start_row < 0:
        return None
    if start_row >= total_rows:
        return None
    if start_col < 0:
        return None
    if start_col >= total_cols:
        return None

    if goal_row < 0:
        return None
    if goal_row >= total_rows:
        return None
    if goal_col < 0:
        return None
    if goal_col >= total_cols:
        return None
    # We know now at this point, the start and
    # goal points are actually valid
    # Check to see if either the start or goal points
    # lie on a obstacle or not.
    # Otherwise no possible solution is available
    if scene[start_row][start_col]:
        return None
    if scene[goal_row][goal_col]:
        return None
    # return the goal solution if both the
    # start and goal coordinates are the same
    # as each other
    if start == goal:
        return [start]
    # counter used to count the total number of moves
    # requried between starting and goal coordinates
    counter = 0
    # A * search : f(n) = g(n) + h(n)
    # priority_queue needed to implement
    # A * search
    frontier = PriorityQueue()
    # retrieve our h(n) value or best educated
    # guess value from the euclidean distance function
    heuristic = find_path_euclidean_heuristic(start, goal)
    # place the current function generated distance, counter value
    # and coordinate posistion into the pq
    frontier.put((0.0 + heuristic , counter, start))
    counter += 1
    # our cost from the starting origin point
    g_funct = {start: 0.0}
    # parent pointer from the previous path
    came_from = {}
    # the set of node we have already accounted
    # for and explored
    done_nodes = set()
    while frontier.empty() is False:
        # pq unpacking of values
        funct, temp, current_value = frontier.get()
        # if the current_value is an element of
        # already explored nodes then continue
        # exploring the priority queue
        if current_value in done_nodes:
            continue
        
        # goal test of where we have an optimal
        # path we wish to return
        if current_value == goal:
            # reconstruct the previous explored
            # path
            explored_path = [current_value]
            # new valid path we can add to list of
            # explored paths
            while current_value != start:
                current_value = came_from[current_value]
                explored_path.append(current_value)
            # ideal return order of moves
            explored_path.reverse()
            return explored_path
        done_nodes.add(current_value)
        # call our neighbor cost function generator and on 
        # each iteration calculate an estimate g score
        # to fully perform a * search
        for nbor, cost in retrieve_neighbors_with_values(current_value, scene):
            estimate_g = g_funct[current_value] + cost
            # if the neibor's path was never recorded previosoly or
            # the guess cost is less than the actually, then we
            # need to run the alogrithm again
            if (nbor not in g_funct) or (estimate_g < g_funct[nbor]):
                came_from[nbor] = current_value
                g_funct[nbor] = estimate_g
                # update the ideal distance
                updated_h = find_path_euclidean_heuristic(nbor, goal)
                # update the pq to include the new heuristic value,
                # distance from points
                frontier.put((estimate_g + updated_h, counter, nbor))
                counter += 1
    # if we reaach this point, then there is no path between the start and goal
    # points that avoids obstacles
    return None


def find_path_euclidean_heuristic(start, goal):
    # heurstic function for find_path function
    # using the euclidean distance formula
    # sqrt((x2 - x1)^2 + (y2 - y1)^2)
    # start is tuple of coordinates with
    # (row, column) for the point
    start_row = start[0]
    start_col = start[1]
    # goal is tuple of coordinates with
    # (row, column) for the point
    goal_row = goal[0]
    goal_col = goal[1]
    # sum of squares
    sum_of_squares = (goal_row - start_row) ** 2
    sum_of_squares += (goal_col - start_col) ** 2
    euclid_dist = math.sqrt(sum_of_squares)
    return euclid_dist


def retrieve_neighbors_with_values(pt, scene):

    # Given a current point (row, col) and a scene grid of booleans,
    # generate (neighbor_point, step_cost) for all valid moves.

    # Valid moves: 8-directional (U, D, R, L, and diagonals)
    # Cost: 1.0 for normal moves, sqrt(2) for diagonal
    # as according to euclidean distances

    # prelimnary work to setup the function correclty
    row = pt[0]
    col = pt[1]
    total_rows = len(scene)
    total_cols = len(scene[0])

    # possible direction coordinate points
    # based on the orgin point at (0,0)

    # up, down, left, right, up-left,
    # up-right, down-left, down-right
    possible_directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                           (-1, -1), (-1, 1), (1, -1), (1, 1)]
    # iterate through diretional list of tuples
    for direction in possible_directions:
        dr = direction[0]
        dc = direction[1]
        # perfrom the move cost on the point
        new_row = row + dr
        new_col = col + dc

        # check after the move, we are currently
        # in bounds or not
        # if so, continue to the next move
        if new_row < 0 or new_row >= total_rows:
            continue
        if new_col < 0 or new_col >= total_cols:
            continue

        # 2) obstacle check (destination cell must be free)
        # if empty, then free otherwise True value,
        # move to the next coordinate
        if scene[new_row][new_col]:
            continue

        # cost of the move calculation
        # we know if we moved in a linear
        # direction as opposed to a diaognal
        # direction based on if one of the directional
        # cols or rows is 0 or not
        if dr == 0 or dc == 0:
            cost_of_move = 1.0
        else:
            # diagonal move, not unit move
            cost_of_move = math.sqrt(2)

        # generate the cost of the move in the loop
        # iteration if we make it this far
        yield (new_row, new_col), cost_of_move


# Test case for the find path function:
scene = [[False, False, False],
         [False, True, False],
         [False, False, False]]
print(find_path((0, 0), (2, 1), scene))
scene = [[False, True, False],
         [False, True, False],
         [False, True, False]]
print(find_path((0, 0), (0, 2), scene))


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
