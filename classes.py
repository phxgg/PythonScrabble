import os
import sys
import itertools
import json
from random import shuffle
from datetime import datetime


class Settings:
  def __init__(self) -> None:
    self.computer_algorithm = 'min'
  
  def __repr__(self) -> str:
    return f'[ Settings ] Algorithm: {self.get_computer_algorithm()}'
  
  def get_computer_algorithm(self) -> str:
    return self.computer_algorithm

  def set_computer_algorithm(self, algorithm: str) -> None:
    self.computer_algorithm = algorithm


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

  def __init__(self) -> None:
    '''
    Initialize the bag with all letters. After that, randomize the letters in the bag.
    '''
    
    for letter in self.letters:
      for i in range(self.letters[letter][0]):
        self.bag.append(letter)

    self.randomize_sak()

  @staticmethod
  def get_letter_value(letter: str) -> int:
    '''
    Return the value of a letter.
    '''

    return SakClass.letters[letter][1]

  @staticmethod
  def get_word_value(word: str) -> int:
    '''
    Return the value of a word.
    '''

    value = 0
    for letter in word:
      value += SakClass.get_letter_value(letter)
    return value

  def get_letters(self) -> list:
    '''
    Returns 7 random letters from the bag and removes those letters from the bag.
    '''

    letters = []
    for i in range(7):
      try:
        letters.append(self.bag.pop())
      except IndexError:
        break
    return letters

  def get_letter(self) -> str:
    '''
    Returns a random letter from the bag and removes that letter from the bag.
    '''

    try:
      return self.bag.pop()
    except IndexError:
      return None

  def put_back_letters(self, letters: list) -> None:
    '''
    Puts back the letters in the bag. After that, randomizes the letters in the bag.
    '''

    for letter in letters:
      self.bag.append(letter)

    self.randomize_sak()

  def randomize_sak(self) -> None:
    '''
    Randomizes (shuffles) the letters in the bag.
    '''

    shuffle(self.bag)

  def number_of_letters(self) -> int:
    '''
    Returns the number of letters remaining in the bag.
    '''

    return len(self.bag)


class Player:
  def __init__(self, name: str, sak: SakClass, end_game: list) -> None:
    self.letters = []
    self.score = 0
    self.name = name
    self.sak = sak
    self.end_game = end_game
    self.current_message = ''
  
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
    self.current_message = ''

    # Create wordlist if it does not already exist
    global wordlist
    if 'wordlist' not in globals():
      # print('[ DEBUG ] Variable \'wordlist\' not in globals')
      wordlist = open('greek7.txt', 'r', encoding='utf-8').read().splitlines()
    
    # Check if word is greater than 7 letters
    if len(word) > 7:
      self.current_message = 'Η λέξη είναι μεγαλύτερη από 7 χαρακτήρες!'
      return False

    # Check if word's letters are in player's letters
    letters_copy = self.get_letters().copy()
    for letter in word:
      if letter in letters_copy:
        letters_copy.remove(letter)
      else:
        self.current_message = f'Το γράμμα {letter} δεν υπάρχει στα γράμματα σου!'
        return False

    # Check if word is in dictionary
    if not word in wordlist:
      self.current_message = f'Η λέξη {word} δεν υπάρχει στο λεξικό!'
      return False
    
    # Word is valid
    return True

  def evaluate_word(self, word) -> tuple:
    '''
    Evaluate word.
    If the word is valid, add it to the player's score and remove the letters from the player's letters.
    Return: (bool: whether the word was evaluated, str: message to display)
    '''

    if not self.is_valid_word(word):
      return False, self.current_message

    # self.increase_score(SakClass.get_word_value(word))
    for letter in word:
      self.remove_letter(letter)
      self.increase_score(SakClass.get_letter_value(letter))
      self.add_remaining_letters()

    return True, ''


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

        eval, msg = self.evaluate_word(word)
        
        if eval:
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

        eval, msg = self.evaluate_word(word)

        if eval:
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
    approved_words = {}

    for i in range(1, len(self.get_letters())): # words of 2 - numOfLetters letters
      for x in itertools.permutations(self.get_letters(), i + 1):
        word = ''.join(x)
        if self.is_valid_word(word):
          # add word to approved_words with value of word
          # return False, self.current_message
          approved_words[word] = SakClass.get_word_value(word)

    if len(approved_words) > 0:
      # find max value in approved_words
      max_value_word = max(approved_words, key=approved_words.get)
      
      eval, msg = self.evaluate_word(max_value_word)

      if eval:
        self.set_letters(self.sak.get_letters())
        self.sak.put_back_letters(self.get_letters())
        print(f'[ {self.get_name()} ] Λέξη: {max_value_word} - Κερδίζεις {approved_words[max_value_word]} πόντους!')
        print(f'[ {self.get_name()} ] >>> Νέα γράμματα: *κρυφό*') # {self.get_letters()}
        print('--------------------')
        return
    else:
      print('Δεν βρέθηκε κάποια λέξη. Τέλος παιχνιδιού.')
      self.end_game[0] = True
      return


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


class Game:
  def __init__(self, settings: Settings) -> None:
    '''
    Initializes the game variables.
    Afterwards setup() is called to setup the game.
    '''

    self.clear_screen()
    print('[!] Νέο παιχνίδι!')

    self.sak = SakClass()
    self.settings = settings
    self.round = 1
    self.end_game = [False] # enclose the inout variable so we can actually pass by reference into the Player class

    self.setup()

  def __repr__(self) -> str:
    return f'[ Game ] Round: {self.round}\n{repr(self.human)}\n{repr(self.computer)}\nGame has ended: {self.end_game[0]}\n{repr(self.settings)}'

  @staticmethod
  def clear_screen() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

  def setup(self) -> None:
    '''
    Initalizes human and computer and set each player's letters.
    Afterwards run() is called to start the game.
    '''

    # Get player name & initialize player and computer
    player_name = input('Πληκτρολογήστε το όνομα σας: ')
    self.human = Human(name=player_name, sak=self.sak, end_game=self.end_game)
    self.computer = Computer(sak=self.sak, end_game=self.end_game, algorithm=self.settings.get_computer_algorithm())

    # Set letters for players
    self.human.set_letters(self.sak.get_letters())
    self.computer.set_letters(self.sak.get_letters())

    # Run game
    self.run()

  def run(self) -> None:
    '''
    Starts a loop that runs until the self.end_game[0] is True.
    Each loop is a new round, and each round is played by the human and then the computer.
    '''

    while True:
      if self.end_game[0] == True:
        self.end()
        break

      print('\n** [ Round ', self.round, '] Διαθέσιμα γράμματα:', self.sak.number_of_letters(), ' **')
      print('*******************************************')
      print(repr(self.human))
      print('*******************************************')
      print(repr(self.computer))

      self.human.play()

      # if human has pressed 'q' then end the game, otherwise continue
      if self.end_game[0] == True:
        self.end()
      else:
        self.computer.play()
        self.round += 1

  def end(self) -> None:
    '''
    Prints the winner and the final score.
    Also saves the game to the game logs folder.
    '''

    print('\n[ INFO ] Τέλος παιχνιδιού!\n')
    
    game_log = GameLog(
        [self.human.get_name(), self.computer.get_name()],
        [self.human.get_score(), self.computer.get_score()],
        self.round,
        101-self.sak.number_of_letters()
      )

    # display game info
    print('*******************************************')
    print(f'** [ Winner: {game_log.get_winner()} ]')
    print(f'** Total Rounds: {game_log.get_rounds()}')
    print(f'** Total Letters Used: {game_log.get_letters_used()}')
    print(f'** Total Letters Used: {game_log.get_letters_used()}')
    print(f'** Date: {game_log.get_date()}')
    print('*******************************************')

    game_log.save()
    sys.exit()


class GameLog:
  def __init__(self, players: list, scores: list, rounds: int, letters_used: int) -> None:
    self.players = players
    self.scores = scores
    self.rounds = rounds
    self.letters_used = letters_used
    self.date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    if scores[0] > scores[1]:
      self.winner = players[0]
    elif scores[0] < scores[1]:
      self.winner = players[1]
    else:
      self.winner = 'DRAW'

  def get_players(self) -> list:
    return self.players
  
  def get_scores(self) -> list:
    return self.scores

  def get_rounds(self) -> int:
    return self.rounds

  def get_letters_used(self) -> int:
    return self.letters_used
  
  def get_winner(self) -> str:
    return self.winner

  def get_date(self) -> str:
    return self.date

  def save(self) -> None:
    '''
    Saves the game log to a json file in the game_logs directory.
    '''

    if not os.path.exists('game_logs/'):
      os.makedirs('game_logs/')

    file_name = self.date.replace('/', '-').replace(':', '-') + '.json'
    with open(f'game_logs/{file_name}', 'w+') as f:
      json.dump(self.__dict__, f)

  @staticmethod
  def load(game_log_path: str):
    '''
    Loads a game log from a json file.
    '''

    game_log = None
    with open(game_log_path, 'r') as f:
      game_log = json.load(f)
    return game_log

