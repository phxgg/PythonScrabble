import os
import sys
from classes.Computer import Computer
from classes.GameLog import GameLog
from classes.Human import Human
from classes.SakClass import SakClass
from classes.Settings import Settings


class Game:
  def __init__(self, settings: Settings) -> None:
    '''
    Initializes the game variables.
    Afterwards setup() is called to setup the game.
    '''

    self.clear_screen()
    print('[!] Νέο παιχνίδι!')

    self.sak = SakClass()
    self.settings = settings
    self.round = 1
    self.end_game = [False] # enclose the inout variable so we can actually pass by reference into the Player class

    self.setup()

  def __repr__(self) -> str:
    return f'[ Game ] Round: {self.round}\n{repr(self.human)}\n{repr(self.computer)}\nGame has ended: {self.end_game[0]}\n{repr(self.settings)}'

  @staticmethod
  def clear_screen() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

  def setup(self) -> None:
    '''
    Initalizes human and computer and set each player's letters.
    Afterwards run() is called to start the game.
    '''

    # Get player name & initialize player and computer
    player_name = input('Πληκτρολογήστε το όνομα σας: ')
    self.human = Human(name=player_name, sak=self.sak, end_game=self.end_game)
    self.computer = Computer(sak=self.sak, end_game=self.end_game, algorithm=self.settings.get_computer_algorithm())

    # Set letters for players
    self.human.set_letters(self.sak.get_letters())
    self.computer.set_letters(self.sak.get_letters())

    # Run game
    self.run()

  def run(self) -> None:
    '''
    Starts a loop that runs until the self.end_game[0] is True.
    Each loop is a new round, and each round is played by the human and then the computer.
    '''

    while True:
      if self.end_game[0] == True:
        self.end()
        break

      print('\n** [ Round ', self.round, '] Διαθέσιμα γράμματα:', self.sak.number_of_letters(), ' **')
      print('*******************************************')
      print(repr(self.human))
      print('*******************************************')
      print(repr(self.computer))

      self.human.play()

      # if human has pressed 'q' then end the game, otherwise continue
      if self.end_game[0] == True:
        self.end()
      else:
        self.computer.play()
        self.round += 1

  def end(self) -> None:
    '''
    Prints the winner and the final score.
    Also saves the game to the game logs folder.
    '''

    print('\n[ INFO ] Τέλος παιχνιδιού!\n')
    
    game_log = GameLog(
        [self.human.get_name(), self.computer.get_name()],
        [self.human.get_score(), self.computer.get_score()],
        self.round,
        101-self.sak.number_of_letters()
      )

    # display game info
    print('*******************************************')
    print(f'** [ Winner: {game_log.get_winner()} ]')
    print(f'** Total Rounds: {game_log.get_rounds()}')
    print(f'** Total Letters Used: {game_log.get_letters_used()}')
    print(f'** Total Letters Used: {game_log.get_letters_used()}')
    print(f'** Date: {game_log.get_date()}')
    print('*******************************************')

    game_log.save()
    sys.exit()

