class Board:
  def __init__(self, cells=[" ", " ", " ", " ", " ", " ", " ", " ", " "]):
    self.cells = cells


  def display(self):
    print(f" {self.cells[0]} | {self.cells[1]} | {self.cells[2]} ")
    print("-----------")
    print(f" {self.cells[3]} | {self.cells[4]} | {self.cells[5]} ")
    print("-----------")
    print(f" {self.cells[6]} | {self.cells[7]} | {self.cells[8]} ")

  def update(self, user_input, token):
    idx = int(user_input) - 1
    self.cells[idx] = token

  def valid_position(self, user_input):
    idx = int(user_input) - 1
    if(self.cells[idx] == " "):
      return True
    else:
      return False
    
  def full(self):
    if(self.token_count() == 9):
      return True
    else:
      return False

  def token_count(self):
    tokens = [cell for cell in self.cells if cell != " "]
    return len(tokens)