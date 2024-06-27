import subprocess

def clear_cli():
  subprocess.run("clear")

def get_input():
  return input("Input Here: ")

def invalid_input():
  print("Incorrect input... Try again!")