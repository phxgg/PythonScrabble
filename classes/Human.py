from classes.Player import Player
from classes.SakClass import SakClass


class Human(Player):
  def __init__(self, name: str, sak: SakClass, end_game: list) -> None:
    super().__init__(name=name, sak=sak, end_game=end_game)

  def __repr__(self) -> str:    
    return f'[ INFO ] Παίχτης: {self.get_name()}\n[ INFO ] Γράμματα: {self.get_letters_with_value()}\n[ INFO ] Σκορ: {self.get_score()}'

  def handle_word_input(self) -> None:
    # Get player input
    word = input('Πληκτρολογήστε μία λέξη: ')

    if word == 'p':
      self.set_letters(self.sak.get_letters())
      self.sak.put_back_letters(self.get_letters())
      print('Τα γράμματα επαναφέρθηκαν, ωστόσο χάνεις τη σειρά σου.')
      return
    elif word == 'q':
      self.end_game[0] = True
      return
      # TODO: save the game
      # sys.exit()

    if self.evaluate_word(word):
      print('--------------------')
      print(f'[ {self.get_name()} ] Λέξη: {word} - Κέρδισες {SakClass.get_word_value(word)} πόντους!')
      print(f'[ {self.get_name()} ] Νέα γράμματα: {self.get_letters()}')
      print('--------------------')
    else:
      self.handle_word_input()

  def play(self) -> None:
    print('--------------------')
    print('Παίζεις! ** Σκορ:', self.get_score(), ' **')
    print('Γράμματα: ', self.get_letters())

    self.handle_word_input()

  