# Tic-Tac-Toe
A nice game of Tic-Tac-Toe

## Basic Game
Supports up to two human players.

AI Player class implements MiniMax with Alpha-Beta pruning for perfect play.

## Incomplete Information Tic-Tac-Toe
### !WORK IN PROGRESS!
Inspired by [https://www.smbc-comics.com/comic/incomplete]():

Played over multiple rounds of Tic-Tac-Toe. Players alternate who goes first.

At the start of each round, players are assigned a random goal which is concealed from their opponent:
 - Win
 - Draw
 - Lose

At the end of the round, each player which achieved their goal is awarded a point.

The winner is the first player to reach 5 points. Or the player who would go first in the next round in the case of a tie.