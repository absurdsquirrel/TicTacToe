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
