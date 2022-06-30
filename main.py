import sys

from classes.Game import Game

def handle_menu_input():
  choice = input('Επιλέξτε: ')

  if choice == '1':
    print('Σκορ')
  elif choice == '2':
    print('Ρυθμίσεις')
  elif choice == '3':
    # Start the game
    game = Game()
  elif choice == 'q':
    print('Έξοδος')
    sys.exit()
  else:
    print('Λάθος επιλογή')
    handle_menu_input()

def main():
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