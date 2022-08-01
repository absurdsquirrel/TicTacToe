class Game:
    def __init__(self, player0, player1):
        self.board = [[" "] * 3 for _ in range(3)]
        self.empty_squares = 9
        self.marks = ["X", "O"]
        self.players = [player0, player1]
        self.current_player = player0

    def other_player(self, player):
        return self.players[(player.player_num + 1) % 2]

    def is_valid_move(self, move):
        if move not in range(9):
            return False
        r, c = divmod(move, 3)
        return self.board[r][c] == " "

    def undo_player_move(self, player, move):
        if player is self.current_player:
            raise ValueError(f"player {player.player_num} was not the previous player")
        if move not in range(9):
            raise ValueError(f"{move + 1} is not a valid square")
        r, c = divmod(move, 3)
        if self.board[r][c] != self.marks[player.player_num]:
            raise ValueError(f"player {player.player_num} did not play {move}")
        self.board[r][c] = " "
        self.empty_squares += 1
        self.current_player = self.other_player(player)

    def player_move(self, player, move):
        if player is not self.current_player:
            raise ValueError(f"player {player.player_num} is not the current player")
        if not self.is_valid_move(move):
            raise ValueError(f"{move + 1} is not an empty square")
        print(f"{self.marks[player.player_num]} plays {move + 1}")
        r, c = divmod(move, 3)
        self.board[r][c] = self.marks[player.player_num]
        self.empty_squares -= 1
        self.current_player = self.other_player(player)

    @staticmethod
    def end_game(winner):
        print("Game over.")
        print(f"Winner: {winner}")

    def evaluate_board(self, move, board):
        """
        :param self:
        :param move: int representing the last move made
        :param board: the board the move was played on
        :return: tuple (bool, str) representing (game_over, winner), winner is None on a tie or if game not over
        """
        if move is None:
            return False, None

        r, c = divmod(move, 3)
        mark = board[r][c]
        if mark not in self.marks:
            return False, None
        # if latest move completed a line, declare winner
        # check move column
        if all(board[(r + i) % 3][c] == mark for i in range(3)):
            return True, mark  # (game_over, winner)
        # check move row
        if all(board[r][(c + j) % 3] == mark for j in range(3)):
            return True, mark
        # check diagonals
        if move in [0, 4, 8] and all(board[(r + i) % 3][(c + i) % 3] == mark for i in range(3)):
            return True, mark
        if move in [2, 4, 6] and all(board[(r + i) % 3][(c - i) % 3] == mark for i in range(3)):
            return True, mark
        # elif board is full, declare tie
        if not self.empty_squares:
            return True, None
        # else game continues
        return False, None

    def print_board(self):
        print(f" {self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]}")
        print("---+---+---")
        print(f" {self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]}")
        print("---+---+---")
        print(f" {self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]}")

    def play_game(self):
        winner = None
        game_over = False
        while not game_over:
            self.print_board()
            # ask current player for move
            print(f"Move for {self.marks[self.current_player.player_num]}? [1-9]")
            move = self.current_player.move(self.board)
            # play move
            try:
                self.player_move(self.current_player, move)
                game_over, winner = self.evaluate_board(move, self.board)
            except ValueError as e:
                print(e)
                # AI automatically loses if it makes an illegal move
                if not isinstance(self.current_player, HumanPlayer):
                    self.end_game(self.other_player(self.current_player))
            # check for game over
        self.print_board()
        self.end_game(winner)


class Player:
    def __init__(self, *args, **kwargs):
        self.player_num = args[0]
        self.goal = kwargs["goal"]
        pass

    def move(self, board):
        raise NotImplementedError


class HumanPlayer(Player):
    def __init__(self, player_num, *, goal="win"):
        Player.__init__(self, player_num, goal=goal)

    def move(self, board):
        move = input()
        while not move.isdigit():
            print(f"{move} is not valid. Must be a number from 1 to 9")
            move = input()
        return int(move) - 1


class LowestIndexPlayer(Player):
    """
    Bad AI player for testing purposes
    """
    def __init__(self, player_num, *, goal="win"):
        Player.__init__(self, player_num, goal=goal)
        self.available_moves = []

    def find_moves(self, board):
        self.available_moves = [i for i in range(9) if board[i // 3][i % 3] == " "]

    def move(self, board):
        self.find_moves(board)
        return self.available_moves[0]
