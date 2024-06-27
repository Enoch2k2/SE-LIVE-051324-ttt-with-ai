from helpers import clear_cli, get_input, invalid_input
from board import Board
from game import Game
from human import Human

class Cli:
  def start(self):
    clear_cli()
    print("Welcome to Tic Tac Toe with AI!")
    print("--------")
    print("")
    self.game_mode_menu()
  
  def game_mode_menu(self):
    print("Game Mode Selection")
    print("type '1' to play one player")
    print("type '2' to play two players")
    print("type '3' to play computer vs computer")
    print("type 'exit' to exit program")
    print("")
    self.game_mode_selection()

  def game_mode_selection(self):
    user_input = get_input()
    if user_input == "1":
      print("Playing a one player game...")
    elif user_input == "2":
      board = Board()
      player_1 = Human(token="X")
      player_2 = Human(token="O")
      game = Game(
        player_1=player_1,
        player_2=player_2,
        board=board
        )
      game.start()

    elif user_input == "3":
      print("Playing computer vs computer...")
    elif user_input == "exit":
      print("Thanks for playing! Goodbye!")
    else:
      clear_cli()
      invalid_input()
      self.game_mode_menu()
