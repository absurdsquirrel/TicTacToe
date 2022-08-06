import random


class Player:
    def __init__(self, *args, **kwargs):
        self._player_num = args[0]
        self._goal = kwargs.get("goal", "win")
        self._is_human = False
        self._available_moves = []
        self.points = 0

    def random_goal(self, debug=False):
        goals = ["win", "draw", "lose"]
        self._goal = random.choice(goals)
        if debug or self.is_human:
            print(f"{self} has goal: {self.goal}")

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


class MiniMaxPlayer(Player):
    from TicTacToe.Game import Game

    def __init__(self, player_num, *, goal="win", game: Game, **kwargs):
        Player.__init__(self, player_num, goal=goal, **kwargs)
        self.game = game
        self.mark = ["X", "O"][player_num]

    def move(self, board):
        self.find_moves(board)
        best_val = -1000
        best_move = -1
        silent = True
        for move in self.available_moves:
            self.game.player_move(self, move, silent=silent)
            move_val = self.minimax(move, 0, self.game.other_player(self), silent=silent)
            self.game.undo_player_move(self, move, silent=silent)
            if move_val > best_val:
                best_val = move_val
                best_move = move
        return best_move

    def minimax(self, move, depth, player, *, silent=True, alpha=-1000, beta=1000):
        game_over, winner = self.game.evaluate_board(move)
        inf = 1000
        if game_over:
            if winner is None:      # draw
                return 0
            elif winner == self:    # win
                return inf - depth
            else:                   # lose
                return -inf + depth

        self.find_moves(self.game.board)
        # Maximizer
        if player is self:
            best = -inf
            for move in self.available_moves:
                self.game.player_move(player, move, silent=silent)
                best = max(best, self.minimax(move, depth + 1, self.game.other_player(player),
                                              silent=silent, alpha=alpha, beta=beta))
                alpha = max(alpha, best)
                self.game.undo_player_move(player, move, silent=silent)

                if beta <= alpha:
                    break
        # Minimizer
        else:
            best = inf
            for move in self.available_moves:
                self.game.player_move(player, move, silent=silent)
                best = min(best, self.minimax(move, depth + 1, self.game.other_player(player),
                                              silent=silent, alpha=alpha, beta=beta))
                beta = min(beta, best)
                self.game.undo_player_move(player, move, silent=silent)

                if beta <= alpha:
                    break
        return best


class HumanPlayer(Player):
    def __init__(self, player_num, *, goal="win", **kwargs):
        Player.__init__(self, player_num, goal=goal, **kwargs)
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
    def __init__(self, player_num, *, goal="win", **kwargs):
        Player.__init__(self, player_num, goal=goal)

    def move(self, board):
        self.find_moves(board)
        return self.available_moves[0]


class RandomPlayer(LowestIndexPlayer):
    def __init__(self, player_num, *, goal="win", seed=None, **kwargs):
        LowestIndexPlayer.__init__(self, player_num, goal=goal, **kwargs)
        random.seed(a=seed)

    def move(self, board):
        self.find_moves(board)
        return random.choice(self.available_moves)


class InvalidMovePlayer(Player):
    """
    Always plays 4 to invoke invalid move handling for AI
    """
    def __init__(self, player_num, *, goal="win", **kwargs):
        Player.__init__(self, player_num, goal=goal, **kwargs)

    def move(self, board):
        return 4
