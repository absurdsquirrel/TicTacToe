class Game:
    def __init__(self):
        self.board = [[" "] * 3 for _ in range(3)]
        self.empty_squares = 9
        self.players = ["X", "O"]
        self.current_player = 0

    @staticmethod
    def other_player(player):
        return (player + 1) % 2

    def is_valid_move(self, move):
        if move not in range(9):
            return False
        r, c = divmod(move, 3)
        return self.board[r][c] == " "

    def player_move(self, player, move):
        if player != self.current_player:
            raise ValueError(f"player {player} is not the current player")
        if not self.is_valid_move(move):
            raise ValueError(f"{move + 1} is not an empty square")
        r, c = divmod(move, 3)
        self.board[r][c] = self.players[player]
        self.empty_squares -= 1
        self.current_player = self.other_player(player)

    @staticmethod
    def end_game(winner):
        print("Game over.")
        print(f"Winner: {winner}")

    def evaluate_board(self, move):
        """
        :param self:
        :param move: int representing the last move made
        :return: tuple (bool, str) representing (game_over, winner), winner is None on a tie or if game not over
        """
        if move is None:
            return False, None

        r, c = divmod(move, 3)
        player = self.board[r][c]
        if player not in self.players:
            return False, None
        # if latest move completed a line, declare winner
        # check move column
        if all(self.board[(r + i) % 3][c] == player for i in range(3)):
            return True, player  # (game_over, winner)
        # check move row
        if all(self.board[r][(c + j) % 3] == player for j in range(3)):
            return True, player
        # check diagonals
        if move in [0, 4, 8] and all(self.board[(r + i) % 3][(c + i) % 3] == player for i in range(3)):
            return True, player
        if move in [2, 4, 6] and all(self.board[(r + i) % 3][(c - i) % 3] == player for i in range(3)):
            return True, player
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

        # TODO: implement player class to abstract human vs computer agents
        # for now, just assume human vs human
        winner = None
        game_over = False
        while not game_over:
            self.print_board()
            # ask current player for move
            print(f"Move for {self.players[self.current_player]}? [1-9]")
            move = int(input()) - 1
            # play move
            try:
                self.player_move(self.current_player, move)
            except ValueError as e:
                print(e)
            # check for game over
            game_over, winner = self.evaluate_board(move)
        self.print_board()
        self.end_game(winner)
