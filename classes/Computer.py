from classes.Player import Player
from classes.SakClass import SakClass


class Computer(Player):
  def __init__(self, sak: SakClass, end_game: bool) -> None:
    super().__init__(name='Η/Υ', sak=sak, end_game=end_game)

  def __repr__(self) -> str:
    return f'[ INFO ] Παίχτης: {self.get_name()}\n[ INFO ] Γράμματα: *κρυφό*\n[ INFO ] Σκορ: {self.get_score()}'

  def play(self) -> None:
    print('--------------------')
    print(f'Παίζει ο {self.get_name()}. ** Σκορ:', self.get_score(), ' **')

  