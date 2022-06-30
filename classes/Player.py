from classes.SakClass import SakClass


class Player:
  letters = []
  score = 0

  def __init__(self, name: str, sak: SakClass, end_game: bool) -> None:
    self.name = name
    self.sak = sak
    self.end_game = end_game
  
  def __repr__(self) -> str:
    return f'Player {self.name} with {self.get_letters()} and score {self.get_score()}'

  def get_letters(self) -> list:
    '''
    Returns player's letters
    '''
    return self.letters

  def get_letters_with_value(self) -> str:
    '''
    Returns player's letters with their value
    '''
    letters_str = ''
    for letter in self.letters:
      letters_str += letter + f',{SakClass.get_letter_value(letter)} - '
    letters_str = letters_str[:-3]
    return letters_str

  def get_name(self) -> str:
    return self.name

  def get_score(self) -> int:
    return self.score
  
  def set_name(self, name) -> None:
    self.name = name
  
  def set_score(self, score) -> None:
    self.score = score

  def increase_score(self, score) -> None:
    self.score += score

  def reset_score(self) -> None:
    self.score = 0
  
  def set_letters(self, letters) -> None:
    self.letters = letters

  def remove_letter(self, letter) -> None:
    self.letters.remove(letter)

  def add_letter(self, letter) -> None:
    self.letters.append(letter)

  def add_remaining_letters(self) -> None:
    '''
    Add remaining letters to player's letters so they're always 7
    '''
    needed_letters = 7 - len(self.get_letters())
    for i in range(needed_letters):
      self.add_letter(self.sak.get_letter())

  def is_valid_word(self, word) -> bool:
    # Create wordlist if it does not already exist
    global wordlist
    if 'wordlist' not in globals():
      # print('[ DEBUG ] Variable \'wordlist\' not in globals')
      wordlist = open('greek7.txt', 'r', encoding='utf-8').read().splitlines()
    
    # Check if word is greater than 7 letters
    if len(word) > 7:
      print('Η λέξη είναι μεγαλύτερη από 7 χαρακτήρες!')
      return False

    # Check if word's letters are in player's letters
    letters_copy = self.get_letters().copy()
    for letter in word:
      if letter in letters_copy:
        letters_copy.remove(letter)
      else:
        print('Το γράμμα ', letter, ' δεν υπάρχει στα γράμματα σου!')
        return False

    # Check if word is in dictionary
    if not word in wordlist:
      print('Η λέξη ', word, ' δεν υπάρχει στο λεξικό!')
      return False
    
    # Word is valid
    return True

  def evaluate_word(self, word) -> bool:
    if not self.is_valid_word(word):
      return False

    # self.increase_score(SakClass.get_word_value(word))
    for letter in word:
      self.remove_letter(letter)
      self.increase_score(SakClass.get_letter_value(letter))
      self.add_remaining_letters()

    return True
