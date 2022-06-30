import os
from classes.Computer import Computer
from classes.Human import Human
from classes.SakClass import SakClass


class Game:
  def __init__(self):
    # Clear console and display new game info
    self.clear_screen()
    print('[!] Νέο παιχνίδι!')

    # Initialize the SakClass
    self.sak = SakClass()
    self.round = 1
    self.setup()

  def __repr__(self) -> str:
    pass

  @staticmethod
  def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

  def setup(self):
    '''
    Setup the game.
    '''
    # Get player name & initialize player and computer
    player_name = input('Πληκτρολογήστε το όνομα σας: ')
    self.human = Human(name=player_name, sak=self.sak)
    self.computer = Computer(sak=self.sak)

    # Set letters for players
    self.human.set_letters(self.sak.get_letters())
    self.computer.set_letters(self.sak.get_letters())

    print('** Διαθέσιμα γράμματα:', self.sak.number_of_letters(), '**')
    print('*************************************')
    print(repr(self.human))
    print('*************************************')
    print(repr(self.computer))

    # Run game
    self.run()

  def run(self):
    # TODO: Game rounds. Player goes first, computer goes second and so on until the game ends.
    self.human.play()

  def end(self):
    pass

