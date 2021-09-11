from random import randint
from art import LOGO
import constant

def get_guess() -> int:
  guess = int(input("Make a guess: "))
  return guess

def normal_game(lives: int):
  number = randint(1, 100)
  game_on = True
  while game_on:
    constant.print_lives(lives)
    guess = get_guess()
    if guess == number:
      game_on = False
    else:
      lives -= 1
      if guess > number:
        constant.print_high()
      else:
        constant.print_low()
      if lives == 0:
        game_on = False
  if lives > 0 and guess != number:
    # Error output
    print("How did we get here?..")
  elif lives > 0:
    constant.print_win(number)
  else:
    constant.print_lose(number)

def unfair_game(lives: int):
  number_from = 1
  number_to = 100
  game_on = True
  win = False
  while game_on:
    constant.print_lives(lives)
    guess = get_guess()
    if number_from == number_to:
      # Only one number left to guess => normal behaviour
      if guess == number_from:
        game_on = False
        win = True
      else:
        lives -= 1
        if guess > number_from:
          constant.print_high
        else:
          constant.print_low()
    elif guess < number_from:
      # Guess is lower than possible
      lives -= 1
      constant.print_low()
    elif guess > number_to:
      # Guess is higher than possible
      lives -= 1
      constant.print_high()
    else:
      # Guess is normal, but there is still wiggle room
      lives -= 1
      if guess - number_from > number_to - guess:
        # More numbers below the guess
        constant.print_high()
        number_to = guess - 1
      elif number_to - guess > guess - number_from:
        # More numbers above the guess
        constant.print_low()
        number_from = guess + 1
      else:
        is_up = randint(0, 1) == 1
        if is_up:
          constant.print_low()
          number_from = guess + 1
        else:
          constant.print_high()
          number_to = guess - 1

    if lives == 0:
      game_on = False
  
  if win:
    constant.print_win(guess)
  else:
    constant.print_lose(number_from)


print(LOGO)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100")

game = {
  constant.GAMEMODE_NORMAL: normal_game,
  constant.GAMEMODE_UNFAIR: unfair_game,
}

difficulties = {
  constant.DIFFICULTY_EASY: 10,
  constant.DIFFICULTY_HARD: 5,
}

gamemode = input(constant.GAMEMODE_TEXT).lower()
while gamemode not in [constant.GAMEMODE_NORMAL, constant.GAMEMODE_UNFAIR]:
  gamemode = input(constant.GAMEMODE_TEXT).lower()

difficulty = input(constant.DIFFICULTY_TEXT).lower()
while difficulty not in [constant.DIFFICULTY_EASY, constant.DIFFICULTY_HARD]:
  difficulty = input(constant.DIFFICULTY_TEXT).lower()

lives = difficulties[difficulty]
game[gamemode](lives)

print("Thank you for playing!")

