from player import Player
import ipdb
import random

class Computer(Player):
  def move(self, board):
    list_of_valid_moves = board.valid_positions()
    return str(random.choice(list_of_valid_moves) + 1)
    
  def find_winning_move(self, board):
    # find a winning spot int he board
    pass

  def defend(self, board):
    # try to block the player!
    pass

  def random_move(self, board):
    # otherwise make random move
    pass