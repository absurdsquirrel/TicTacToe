def game():
    def __init__(self):
        self.board = [[" "] * 3 for _ in range(3)]
        self.empty_squares = 9
        self.players = ["X", "O"]
        self.current_player = 0

    def other_player(self, player):
        return self.players[(player + 1) % 2]

    def is_valid_move(self, move):
        r, c = divmod(move, 3)
        return self.board[r][c] == " "

    def player_move(self, player, move):
        if player != self.current_player:
            raise ValueError(f"player {player} is not the current player")
        if not self.is_valid_move(move):
            raise ValueError(f"{move} is not an empty square")
        r, c = divmod(move, 3)
        self.board[r][c] = self.players[player]
        self.empty_squares -= 1
        # TODO: check for game over
        self.current_player = self.other_player(player)

    def evaluate_board(self, move):
        """
        :param self:
        :param move: int representing the last move made
        :return: tuple (bool, str) representing (game_over, winner), winner is None on a tie or if game not over
        """
        r, c = divmod(move, 3)
        player = self.board[r][c]
        # if latest move completed a line, declare winner
        # check move column
        if all(self.board[(r + i) % 3][c] == player for i in range(1, 3)):
            return True, player  # (game_over, winner)
        # check move row
        if all(self.board[r][(c + j) % 3] == player for j in range(1, 3)):
            return True, player
        # check diagonals
        if move in [0, 4, 8] and all(self.board[(r + i) % 3][(c + i) % 3] == player for i in range(1, 3)):
            return True, player
        if move in [2, 4, 6] and all(self.board[(r + i) % 3][(c - i) % 3] == player for i in range(1, 3)):
            return True, player
        # elif board is full, declare tie
        if not self.empty_squares:
            return True, None
        # else game continues
        return False, None

    def print_board(self):
        # TODO: print board
        pass
