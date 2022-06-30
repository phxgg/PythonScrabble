from random import shuffle


class SakClass:
  bag = []

  # Available letters: [letter: [amount, value]]
  letters = {
    'Α': [12, 1],
    'Β': [1, 8],
    'Γ': [2, 4],
    'Δ': [2, 4],
    'Ε': [8, 1],
    'Ζ': [1, 10],
    'Η': [7, 1],
    'Θ': [1, 10],
    'Ι': [8, 1],
    'Κ': [4, 2],
    'Λ': [3, 3],
    'Μ': [3, 3],
    'Ν': [6, 1],
    'Ξ': [1, 10],
    'Ο': [9, 1],
    'Π': [4, 2],
    'Ρ': [5, 2],
    'Σ': [7, 1],
    'Τ': [8, 1],
    'Υ': [4, 2],
    'Φ': [1, 8],
    'Χ': [1, 8],
    'Ψ': [1, 10],
    'Ω': [3, 3]
  }

  def __init__(self):
    for letter in self.letters:
      for i in range(self.letters[letter][0]):
        self.bag.append(letter)

    self.randomize_sak()

  def get_letters(self):
    '''
    Get 7 random letters from the bag and remove them from the bag.
    '''

    letters = []
    for i in range(7):
      letters.append(self.bag.pop())
    return letters

  def put_back_letters(self, letters):
    '''
    Put back the letters in the bag.
    '''

    for letter in letters:
      self.bag.append(letter)

  def randomize_sak(self):
    '''
    Randomize (shuffle) the letters in the bag.
    '''

    shuffle(self.bag)

  def number_of_letters(self):
    '''
    Return the number of letters remaining in the bag.
    '''

    return len(self.bag)

  