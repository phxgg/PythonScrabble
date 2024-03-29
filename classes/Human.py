from classes.Player import Player
from classes.SakClass import SakClass


class Human(Player):
  def __init__(self, name: str, sak: SakClass, end_game: list) -> None:
    super().__init__(name=name, sak=sak, end_game=end_game)

  def __repr__(self) -> str:    
    return f'[ INFO ] Παίχτης: {self.get_name()}\n[ INFO ] Γράμματα: {self.get_letters_with_value()}\n[ INFO ] Σκορ: {self.get_score()}'

  def handle_word_input(self) -> None:
    '''
    Waits for the user to input a word and does all the necessary checks before evaluating it.
    '''

    # Get player input
    word = input(f'[ {self.get_name()} ] Πληκτρολογήστε μία λέξη: ')

    # If user input is 'p', player wants to pass
    # If user input is 'q', player wants to quit
    if word == 'p':
      letters_to_return = self.get_letters().copy()
      self.set_letters(self.sak.get_letters())
      self.sak.put_back_letters(letters_to_return)
      print('> Τα γράμματα επαναφέρθηκαν, ωστόσο χάνεις τη σειρά σου.')
      return
    elif word == 'q':
      self.end_game[0] = True
      return

    eval, msg = self.evaluate_word(word)

    if eval:
      print(f'[ {self.get_name()} ] Λέξη: {word} - Κερδίζεις {SakClass.get_word_value(word)} πόντους!')
      print(f'[ {self.get_name()} ] >>> Νέα γράμματα: {self.get_letters()}')
      print('--------------------')
    else:
      if msg: print(msg)
      self.handle_word_input()

  def play(self) -> None:
    print('\nΠαίζεις! ** Σκορ:', self.get_score(), ' **')
    print('>>> Γράμματα: ', self.get_letters())

    self.handle_word_input()

  