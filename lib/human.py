from helpers import get_input

class Human:
  def __init__(self, token):
    self.token = token

  def move(self):
    return get_input()