from classes.Player import Player
from classes.SakClass import SakClass


class Computer(Player):
  def __init__(self, sak: SakClass):
    super().__init__(name='Η/Υ', sak=sak)

  def __repr__(self) -> str:
    return super().__repr__()

  def play(self):
    pass

  