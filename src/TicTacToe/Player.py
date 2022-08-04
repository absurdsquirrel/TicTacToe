import random


class Player:
    def __init__(self, *args, **kwargs):
        self.player_num = args[0]
        self.goal = kwargs["goal"]
        self._is_human = False

    def __repr__(self):
        return ["X", "O"][self.player_num]

    @property
    def is_human(self) -> bool:
        return self._is_human

    def move(self, board):
        raise NotImplementedError


class HumanPlayer(Player):
    def __init__(self, player_num, *, goal="win"):
        Player.__init__(self, player_num, goal=goal)
        self._is_human = True

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


class RandomPlayer(LowestIndexPlayer):
    def __init__(self, player_num, *, goal="win", seed=None):
        LowestIndexPlayer.__init__(self, player_num=player_num, goal=goal)
        random.seed(a=seed)

    def move(self, board):
        self.find_moves(board)
        return random.choice(self.available_moves)


class InvalidMovePlayer(Player):
    """
    Always plays 4 to invoke invalid move handling for AI
    """
    def __init__(self, player_num, *, goal="win"):
        Player.__init__(self, player_num, goal=goal)

    def move(self, board):
        return 4
