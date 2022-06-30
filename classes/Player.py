from classes.SakClass import SakClass


class Player:
  letters = []
  score = 0

  def __init__(self, name: str, sak: SakClass):
    self.name = name
    self.sak = sak
  
  def __repr__(self) -> str:
    letters_str = ''
    for letter in self.letters:
      letters_str += letter + f',{SakClass.get_letter_value(letter)} - '
    letters_str = letters_str[:-3]
    
    return f'Παίχτης: {self.name}\nΓράμματα: {letters_str}\nΣκορ: {self.score}'

  def get_letters(self):
    return self.letters

  def get_name(self):
    return self.name

  def get_score(self):
    return self.score
  
  def set_name(self, name):
    self.name = name
  
  def set_score(self, score):
    self.score = score

  def increase_score(self, score):
    self.score += score

  def reset_score(self):
    self.score = 0
  
  def set_letters(self, letters):
    self.letters = letters

  def remove_letter(self, letter):
    self.letters.remove(letter)

  def add_letter(self, letter):
    self.letters.append(letter)

  def add_remaining_letters(self):
    '''
    TODO!
    Add remaining letters to player's letters so they're always 7
    '''
    needed_letters = 7 - len(self.get_letters())
    for i in range(needed_letters):
      self.add_letter(self.sak.get_letter())

  def is_valid_word(self, word):
    # Create wordlist if it does not already exist
    global wordlist
    if 'wordlist' not in globals():
      print('Variable \'wordlist\' not in globals')
      wordlist = open('greek7.txt', 'r', encoding='utf-8').read().splitlines()
    
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

  def evaluate_word(self, word):
    if not self.is_valid_word(word):
      return False

    for letter in word:
      self.remove_letter(letter)
      self.increase_score(SakClass.get_word_value(word))
      self.add_remaining_letters()

    return True
