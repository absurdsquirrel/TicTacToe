from TicTacToe import Player, Game


def main():
    # player0 = Player.HumanPlayer(0)
    # player0 = Player.MiniMaxPlayer(0)
    player1 = Player.MiniMaxPlayer(1)
    # player0 = Player.LowestIndexPlayer(0)
    # player0 = Player.InvalidMovePlayer(0)
    player0 = Player.RandomPlayer(0)
    # player1 = Player.RandomPlayer(1)
    my_game = Game.Game(player0, player1)
    # player0.hook_into_game(my_game)
    player1.hook_into_game(my_game)
    my_game.play_game()


if __name__ == '__main__':
    main()
