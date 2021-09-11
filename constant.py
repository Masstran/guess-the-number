GAMEMODE_NORMAL = "normal"
GAMEMODE_UNFAIR = "unfair"
GAMEMODE_TEXT = f"Choose a gamemode. Type '{GAMEMODE_NORMAL}' or '{GAMEMODE_UNFAIR}': "


DIFFICULTY_EASY = "easy"
DIFFICULTY_HARD = "hard"
DIFFICULTY_TEXT = f"Choose a difficulty. Type '{DIFFICULTY_EASY}' or '{DIFFICULTY_HARD}': "

def print_lives(lives: int):
  print(f"You have {lives} lives left.")

def print_win(number: int):
  print(f"Wow! You have won! The number was {number}!!")

def print_lose(number: int):
  print(f"I'm sorry, you lose. The number was {number}.")

def print_high():
  print("Too high.")

def print_low():
  print("Too low.")