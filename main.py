from TicTacToe import Player, Game


def main():
    my_game = Game.Game(Player.RandomPlayer, Player.RandomPlayer)
    my_game.play_game()


if __name__ == '__main__':
    main()
