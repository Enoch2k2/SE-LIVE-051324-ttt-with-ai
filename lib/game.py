import ipdb
from helpers import clear_cli, get_input, invalid_input

class Game:

  win_combinations = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
  ]

  def __init__(self, player_1, player_2, board):
    self.player_1 = player_1
    self.player_2 = player_2
    self.board = board

  def start(self):
    while not self.over():
      clear_cli()
      self.turn()

    if(self.won()):
      print(f"Congratulations {self.winner()}")
    else:
      print("Cat's Game!")

  def turn(self):
    print(f"Player {self.current_player().token} turn")
    self.board.display()
    print("")
    print("Please Enter (1-9): ")
    user_input = self.current_player().move()
    if self.valid_input(user_input) and self.board.valid_position(user_input):
      self.board.update(user_input, self.current_player().token)
      self.board.display()
    else:
      clear_cli()
      invalid_input()
      self.turn()

  def turn_count(self):
    return self.board.token_count()

  def current_player(self):
    return self.player_1 if self.turn_count() % 2 == 0 else self.player_2
  
  def valid_input(self, user_input):
    try:
      idx = int(user_input) - 1
      if(idx in range(9)):
        return True
      else:
        return False
    except:
      return False
    
  def over(self):
    # player won or a draw (aka a cat game)
    if self.draw() or self.won():
      return True
    else:
      return False
    
  def draw(self):
    # not only is the board full, no one won!
    if self.board.full():
      return True
    else:
      return False
    
  def won(self):
    # what details a winner
    for win_combo in Game.win_combinations:
      idx_1 = win_combo[0]
      idx_2 = win_combo[1]
      idx_3 = win_combo[2]

      if self.board.cells[idx_1] != " " and self.board.cells[idx_1] == self.board.cells[idx_2] and self.board.cells[idx_2] == self.board.cells[idx_3]:
        return win_combo
    
    return False
  
  def winner(self):
    idx = self.won()[0]
    return self.board.cells[idx]