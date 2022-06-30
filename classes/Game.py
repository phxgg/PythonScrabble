import os
import sys
from classes.Computer import Computer
from classes.GameLog import GameLog
from classes.Human import Human
from classes.SakClass import SakClass


class Game:
  def __init__(self) -> None:
    self.clear_screen()
    print('[!] Νέο παιχνίδι!')

    # Initialize the SakClass
    self.sak = SakClass()
    self.round = 1
    self.end_game = [False] # enclose the inout variable so we can actually pass by reference into the Player class
    self.setup()

  def __repr__(self) -> str:
    pass

  @staticmethod
  def clear_screen() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

  def setup(self) -> None:
    '''
    Setup the game.
    '''
    # Get player name & initialize player and computer
    player_name = input('Πληκτρολογήστε το όνομα σας: ')
    self.human = Human(name=player_name, sak=self.sak, end_game=self.end_game)
    self.computer = Computer(sak=self.sak, end_game=self.end_game)

    # Set letters for players
    self.human.set_letters(self.sak.get_letters())
    self.computer.set_letters(self.sak.get_letters())

    # Run game
    self.run()

  def run(self) -> None:
    while True:
      if self.end_game[0] == True:
        self.end()
        break

      print('\n** [ Round ', self.round, '] Διαθέσιμα γράμματα:', self.sak.number_of_letters(), ' **')
      print('******************************************')
      print(repr(self.human))
      print('********************************************')
      print(repr(self.computer))

      self.human.play()
      self.computer.play()
      self.round += 1

  def end(self) -> None:
    print('Τέλος παιχνιδιού!')
    
    game_log = GameLog(
        [self.human.get_name(), self.computer.get_name()],
        [self.human.get_score(), self.computer.get_score()],
        self.round,
        101-self.sak.number_of_letters()
      )

    # 

    game_log.save()
    sys.exit()

