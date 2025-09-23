import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_of_x = sum(cell == X for row in board for cell in row)
    count_of_o = sum(cell == O for row in board for cell in row)

    if count_of_x == 0 or count_of_o == count_of_x:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    i = 0
    set_of_actions = set()
    for row in board:
        for j in range(3):
            if row[i] == EMPTY:
                set_of_actions.add((i, j))
        i += 1

    return set_of_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    i, j = action
    if new_board[i][j] == EMPTY:
        if player(board) == X:
            new_board[i][j] = X
        if player(board) == O:
            new_board[i][j] = O
        return new_board
    else:
        raise Exception("Invalid action")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    sum_of_x = [[], [], [], [], []]  # [0][3]-firs diagonal, [0][4]-second diagonal
    sum_of_o = [[], [], [], [], []]  # ^
    n1, n2 = 0, 0

    for row in board:
        n2 -= 1
        if sum(cell == X for cell in row) == 3:
            return X
        if sum(cell == O for cell in row) == 3:
            return O

        for i in range(3):
            if row[i] == X:
                sum_of_x[i].append(1)
            if row[i] == O:
                sum_of_o[i].append(1)
        for j in range(3):
            if sum(sum_of_x[j]) == 3:
                return X
            if sum(sum_of_o[j]) == 3:
                return O

        if row[n1] == X:
            sum_of_x[3].append(1)
        if row[n2] == X:
            sum_of_x[4].append(1)
        if row[n1] == O:
            sum_of_o[3].append(1)
        if row[n2] == O:
            sum_of_o[4].append(1)
        n1 += 1

        if sum(sum_of_x[3]) == 3 or sum(sum_of_x[4]) == 3:
            return X
        if sum(sum_of_o[3]) == 3 or sum(sum_of_o[4]) == 3:
            return O

    if sum(cell == EMPTY for row in board for cell in row) == 0:
        return None

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    count_of_empty = sum(cell == EMPTY for row in board for cell in row)
    if count_of_empty == 0 or winner(board) in (X, O):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    elif winner(board) == EMPTY:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
