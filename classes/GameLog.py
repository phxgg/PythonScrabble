from datetime import datetime
import os
import json

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