from TicTacToe import Player, Game


def main():
    # player0 = HumanPlayer(0)
    # player1 = HumanPlayer(1)
    # player0 = Player.LowestIndexPlayer(0)
    player0 = Player.InvalidMovePlayer(0)
    player1 = Player.RandomPlayer(1)
    my_game = Game.Game(player0, player1)
    my_game.play_game()


if __name__ == '__main__':
    main()
