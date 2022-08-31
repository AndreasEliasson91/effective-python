def color_print(color, text, end='\n'):
    color_dict = {
        "black": 30,
        "red": 31,
        "green": 32,
        "yellow": 33,
        "blue": 34,
        "magenta": 35,
        "cyan": 36,
        "white": 37
    }
    color_string = f"\033[{color_dict[color]}m"
    reset = "\033[0m"
    print(f"{color_string}{text}{reset}", end=end)


def check_horizontal(board: list) -> bool:
    for row in reversed(board):
        counter = 1
        for col in row:
            while counter <= 4:
                if col == row[counter] == row[counter +
                                              1] == row[counter + 2] != 0:
                    return True
                counter += 1
    return False


def check_vertical(board: list) -> bool:
    for col in range(0, 7):
        for row in range((len(board) - 1), 2, -1):
            if board[row][col] == board[row - 1][col] == board[row - \
                2][col] == board[row - 3][col] != 0:
                return True
    return False


def check_diagonal(board: list) -> bool:
    def left_diagonal() -> bool:
        for col in range(3, 7, 1):
            for row in range((len(board) - 1), 2, -1):
                if board[row][col] == board[row -
                                            1][col -
                                               1] == board[row -
                   2][col -
                   2] == board[row -
                   3][col -
                   3] != 0:
                    return True
        return False

    def right_diagonal() -> bool:
        for col in range(3, -1, -1):
            for row in range((len(board) - 1), 2, -1):
                if board[row][col] == board[row -
                                            1][col +
                                               1] == board[row -
                   2][col +
                   2] == board[row -
                   3][col +
                   3] != 0:
                    return True
        return False

    return left_diagonal() or right_diagonal()


def print_board(board: list):
    for i in board:
        for j in i:
            color = "white"
            if j == 1:
                color = "red"
            elif j == 2:
                color = "black"
            color_print(color, "0", end=' ')
        print(end="\n")
    color_print("yellow", "1 2 3 4 5 6 7")


def place_marker(board: list, col: int, active_player: int) -> bool:
    for row in board[::-1]:
        if row[col] == 0:
            row[col] = active_player
            return True
    return False


def victory(board: list) -> bool:
    return check_horizontal(board) or check_vertical(board) or check_diagonal(board)


def main():
    # Comprehension, for _ (ignore) in range(6) print 7 [0] in 6 rows
    board = [[0] * 7 for _ in range(6)]
    active_player = 1
    player_color = ""
    running = True

    while running:
        print_board(board)
        player_color = "Red" if active_player == 1 else "Black"
        move = input(f"\n{player_color}, Choose a column: ")

        if move.isdigit():
            move = int(move)
            if move in range(1, 8):
                move -= 1
                if place_marker(board, move, active_player):
                    if victory(board):
                        running = False
                    else:
                        active_player = 2 if active_player == 1 else 1
                else:
                    color_print("red", "\nThat column is full!\n")
            else:
                color_print("red", "\nNon existing column, try again!\n")
        else:
            color_print(
                "red", "\nInvalid entry!\tType a number between 1 and 7!\n")

    print_board(board)
    print(f"{player_color} wins!")


if __name__ == '__main__':
    main()
