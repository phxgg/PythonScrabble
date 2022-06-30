from datetime import datetime
import os
import json

class GameLog:
  def __init__(self, players: list, scores: list, letters_used: int) -> None:
    self.players = players
    self.scores = scores
    self.letters_used = letters_used
    self.date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    if scores[0] > scores[1]:
      self.winner = players[0]
    elif scores[0] < scores[1]:
      self.winner = players[1]
    else:
      self.winner = 'DRAW'

  def save(self) -> None:
    if not os.path.exists('game_logs/'):
      os.makedirs('game_logs/')

    file_name = self.date.replace('/', '-').replace(':', '-') + '.json'
    with open(f'game_logs/{file_name}', 'w+') as f:
      json.dump(self.__dict__, f)

  @staticmethod
  def load(game_log):
    with open(game_log, 'r') as f:
      game_log = json.load(f)
    return game_log