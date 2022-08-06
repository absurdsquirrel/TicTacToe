from TicTacToe import Player, Game


def main():
    my_game = Game.Game(Player.MiniMaxPlayer, Player.LowestIndexPlayer, smbc=True)
    my_game.play_game()


if __name__ == '__main__':
    main()
