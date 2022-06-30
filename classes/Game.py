import os
from classes.Computer import Computer
from classes.Human import Human
from classes.SakClass import SakClass


class Game:
  def __init__(self):
    # Clear console and display new game info
    self.clear_screen()
    print('[!] Νέο παιχνίδι!')

    self.sak = SakClass()
    self.setup()

  def __repr__(self) -> str:
    pass

  @staticmethod
  def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

  def setup(self):
    # Get player name & initialize player and computer
    player_name = input('Πληκτρολογήστε το όνομα σας: ')
    self.human = Human(name=player_name)
    self.computer = Computer()

    # Set letters for players
    self.human.set_letters(self.sak.get_letters())
    self.computer.set_letters(self.sak.get_letters())

    print(self.human.get_name(), 'έχει', len(self.human.get_letters()), 'γράμματα')
    print(self.human.get_letters())

    print(self.computer.get_name(), 'έχει', len(self.computer.get_letters()), 'γράμματα')
    print(self.computer.get_letters())

  def run(self):
    pass

  def end(self):
    pass

