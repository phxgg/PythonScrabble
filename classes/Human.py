from classes.Player import Player
from classes.SakClass import SakClass


class Human(Player):
  def __init__(self, name):
    super().__init__(name=name)

  def __repr__(self) -> str:
    return super().__repr__()

  def handle_word_input(self):
    # Get player input
    word = input('Πληκτρολογήστε μία λέξη: ')

    if word == 'q':
      print('Τέλος παιχνιδιού!')
      return

    # Check if word is valid & evaluate
    if not self.is_valid_word(word):
      print('Δεν μπορείς να φτιάξεις αυτή τη λέξη!')
      self.handle_word_input()
    else:
      self.evaluate_word(word)

  def play(self):
    print('--------------------')
    print('Παίζεις! ** Σκορ:', self.get_score(), ' **')
    print('Γράμματα: ', self.get_letters())

    self.handle_word_input()

  def is_valid_word(self, word):
    letters_copy = self.get_letters().copy()
    for letter in word:
      if letter in letters_copy:
        letters_copy.remove(letter)
      else:
        print('Το γράμμα ', letter, ' δεν υπάρχει στα γράμματα σου!')
        return False
    return True

  def evaluate_word(self, word):
    for letter in word:
      self.remove_letter(letter)
      self.increase_score(SakClass.get_word_value(word))

    print('Λέξη: ', word, ' - Κέρδισες ', SakClass.get_word_value(word), ' πόντους!')
    print('Γράμματα που παρέμειναν: ', self.get_letters())

  