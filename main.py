import os
import sys

from classes import Game, GameLog, Settings

settings = Settings()

def guidelines():
  '''
  Project PythonScrabble guidelines

  Classes developed:
    Settings
    SakClass
    Player
    Computer
    Human
    Game
    GameLog

  Classes description:
    Settings: Holds the game settings. Right now only the computer algorithm is implemented.
    SakClass: Represents the 'bag of letters', from which you can get, put back, or shuffle letters.
    Player: Represents a player in the game.
    Computer: Inherits the Player class. Implements the computer algorithm.
    Human: Inherits the Player class. Implements how the player plays the game.
    Game: This class will initialize all needed variables to setup, run and end the game.
    GameLog: Save or load game data through this class. Game logs are saved in a JSON file, and loaded as a GameLog object.

  All words are stored in a 'wordlist' global variable, which is a type of list.

  Decorators were used in the SakClass, Game, GameLogs classes to describe static methods.

  Algorithms implemented: Min-Max-Smart
    MIN:
      All possible permutations of the letters are calculated starting from 2 and going up to 7 letters.
      The algorithm will 'play' the first valid word it finds.
    MAX:
      All possible permutations of the letters are calculated starting from 7 and going down to 2 letters.
      The algorithm will 'play' the first valid word it finds.
    SMART:
      All possible permutations of the letters are calculated starting from 2 and going up to 7 letters.
      The algorithm will find all the valid words, then calculate the word that will give the highest score and 'play' it.
  '''
  return

def handle_scores():
  Game.clear_screen()

  print('**** SCORES ****')
  print('----------------')

  logs = {}

  game_logs_dir = 'game_logs/'

  if not os.path.exists('game_logs/'):
    os.makedirs(game_logs_dir)

  i = 0
  for filename in os.listdir(game_logs_dir):
    f = os.path.join(game_logs_dir, filename)
    if os.path.isfile(f):
      game_log = GameLog.load(f)

      logs[i] = game_log
      i += 1
  
  # print table keys
  print('{:<20} {:<15} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}'.format('Date', 'Player 1', 'Player 2', 'Score 1', 'Score 2', 'Winner', 'Rounds', 'Letters Used'))

  # print table rows
  for key, value in logs.items():
    date = value['date']
    player1 = value['players'][0]
    player2 = value['players'][1]
    score1 = value['scores'][0]
    score2 = value['scores'][1]
    winner = value['winner']
    rounds = value['rounds']
    letters_used = value['letters_used']

    print('{:<20} {:<15} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}'.format(date, player1, player2, score1, score2, winner, rounds, letters_used))

  print('\nPress any key to return to the main menu.')
  input()
  main()


# Settings menu
def handle_settings_input():
  Game.clear_screen()

  print('***** Ρυθμίσεις *****')
  print('--------------------')

  min_letters = ('[1]' if settings.get_computer_algorithm() == 'min' else '1.') + ' MIN Letters'
  max_letters = ('[2]' if settings.get_computer_algorithm() == 'max' else '2.') + ' MAX Letters'
  smart = ('[3]' if settings.get_computer_algorithm() == 'smart' else '3.') + ' SMART'

  print(min_letters)
  print(max_letters)
  print(smart)
  print('4. Επιστροφή')

  choice = input('Επιλέξτε αλγόριθμο Η/Υ: ')

  if choice == '1':
    settings.set_computer_algorithm('min')
    handle_settings_input()
  elif choice == '2':
    settings.set_computer_algorithm('max')
    handle_settings_input()
  elif choice == '3':
    settings.set_computer_algorithm('smart')
    handle_settings_input()
  elif choice == '4':
    main()
  else:
    print('Λάθος επιλογή')
    handle_settings_input()

# Main menu
def handle_menu_input():
  choice = input('Επιλέξτε: ')

  if choice == '1':
    handle_scores()
  elif choice == '2':
    handle_settings_input()
  elif choice == '3':
    # Start the game
    game = Game(settings)
  elif choice == 'q':
    print('Έξοδος')
    sys.exit()
  else:
    print('Λάθος επιλογή')
    handle_menu_input()

def main():
  Game.clear_screen()

  help(guidelines)

  # game_log = GameLog.load('game_logs/test.json')
  # print(game_log)

  print('***** SCRABBLE *****')
  print('--------------------')
  print('1. Σκορ')
  print('2. Ρυθμίσεις')
  print('3. Παιχνίδι')
  print('q. Έξοδος')
  print('--------------------')

  handle_menu_input()

if __name__ == '__main__':
  main()