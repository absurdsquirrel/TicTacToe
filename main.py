from TicTacToe import Player, Game


def main():
    my_game = Game.Game(Player.MiniMaxPlayer, Player.MiniMaxPlayer)
    my_game.play_game()


if __name__ == '__main__':
    main()
