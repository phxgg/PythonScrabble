class Player:
  letters = []
  score = 0

  def __init__(self, name):
    self.name = name
  
  def __repr__(self) -> str:
    return f'Player({self.name})'

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
