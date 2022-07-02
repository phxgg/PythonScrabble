import itertools
from classes.Player import Player
from classes.SakClass import SakClass


class Computer(Player):
  def __init__(self, sak: SakClass, end_game: list, algorithm: str) -> None:
    super().__init__(name='Η/Υ', sak=sak, end_game=end_game)
    self.algorithm = algorithm

  def __repr__(self) -> str:
    return f'[ INFO ] Παίχτης: {self.get_name()}\n[ INFO ] Γράμματα: *κρυφό*\n[ INFO ] Σκορ: {self.get_score()}'

  def play(self) -> None:
    print(f'\nΠαίζει ο {self.get_name()}. ** Σκορ: {self.get_score()} **')

    if self.algorithm == 'min':
      self.min()
    elif self.algorithm == 'max':
      self.max()
    elif self.algorithm == 'smart':
      self.smart()

  def min(self) -> None:
    for i in range(1, len(self.get_letters())): # words of 2 - numOfLetters letters
      for x in itertools.permutations(self.get_letters(), i + 1):
        word = ''.join(x)
        if self.evaluate_word(word):
          self.set_letters(self.sak.get_letters())
          self.sak.put_back_letters(self.get_letters())
          print(f'[ {self.get_name()} ] Λέξη: {word} - Κερδίζεις {SakClass.get_word_value(word)} πόντους!')
          print(f'[ {self.get_name()} ] >>> Νέα γράμματα: *κρυφό*') # {self.get_letters()}
          print('--------------------')
          return
        else:
          continue
    
    print('Δεν βρέθηκε κάποια λέξη.')

    if self.sak.number_of_letters() == 0:
      print('Τέλος παιχνιδιού.')
      self.end_game[0] = True
    else:
      letters_to_return = self.get_letters().copy()
      self.set_letters(self.sak.get_letters())
      self.sak.put_back_letters(letters_to_return)
      print('> Ο Η/Υ επανέφερε τα γράμματά του και χάνει τη σειρά του.')

    return

  def max(self) -> None:
    for i in range(len(self.get_letters()), 2, -1): # words of numOfLetters - 2 letters
      for x in itertools.permutations(self.get_letters(), i):
        word = ''.join(x)
        if self.evaluate_word(word):
          self.set_letters(self.sak.get_letters())
          self.sak.put_back_letters(self.get_letters())
          print(f'[ {self.get_name()} ] Λέξη: {word} - Κερδίζεις {SakClass.get_word_value(word)} πόντους!')
          print(f'[ {self.get_name()} ] >>> Νέα γράμματα: *κρυφό*') # {self.get_letters()}
          print('--------------------')
          return
        else:
          continue
    
    print('Δεν βρέθηκε κάποια λέξη. Τέλος παιχνιδιού.')
    self.end_game[0] = True
    return

  def smart(self) -> None:
    pass
  