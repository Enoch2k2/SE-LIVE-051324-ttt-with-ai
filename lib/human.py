from helpers import get_input
from player import Player

class Human(Player):
  def move(self, board):
    return get_input()