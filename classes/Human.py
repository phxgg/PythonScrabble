import sys
from classes.Player import Player
from classes.SakClass import SakClass


class Human(Player):
  def __init__(self, name: str, sak: SakClass):
    super().__init__(name=name, sak=sak)

  def __repr__(self) -> str:
    return super().__repr__()

  def handle_word_input(self):
    # Get player input
    word = input('Πληκτρολογήστε μία λέξη: ')

    if word == 'q':
      print('Τέλος παιχνιδιού!')
      # save the game
      sys.exit()

    if self.evaluate_word(word):
      print('Λέξη: ', word, ' - Κέρδισες ', SakClass.get_word_value(word), ' πόντους!')
      print('Γράμματα που παρέμειναν: ', self.get_letters())
    else:
      self.handle_word_input()

  def play(self):
    print('--------------------')
    print('Παίζεις! ** Σκορ:', self.get_score(), ' **')
    print('Γράμματα: ', self.get_letters())

    self.handle_word_input()

  