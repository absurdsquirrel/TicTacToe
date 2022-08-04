import random


class Player:
    def __init__(self, *args, **kwargs):
        self._player_num = args[0]
        self._goal = kwargs["goal"]
        self._is_human = False
        self._available_moves = []

    @property
    def available_moves(self):
        return self._available_moves

    def find_moves(self, board):
        self._available_moves = [i for i in range(9) if board[i // 3][i % 3] == " "]

    def __repr__(self):
        return ["X", "O"][self.player_num]

    @property
    def player_num(self) -> int:
        return self._player_num

    @property
    def goal(self) -> str:
        return self._goal

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
        self.find_moves(board)
        while not move.isdigit() or (int(move) - 1) not in self.available_moves:
            print(f"{move} is not valid. Available moves:")
            for i in [0, 3, 6]:
                print('{0} {1} {2}'.format(*[am+1 if am in self.available_moves else " " for am in range(i, i+3)]))
            move = input()
        return int(move) - 1


class LowestIndexPlayer(Player):
    """
    Bad AI player for testing purposes
    """
    def __init__(self, player_num, *, goal="win"):
        Player.__init__(self, player_num, goal=goal)

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
