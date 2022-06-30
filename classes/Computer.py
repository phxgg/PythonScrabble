from classes.Player import Player


class Computer(Player):
  def __init__(self):
    super().__init__(name='Η/Υ')

  def __repr__(self) -> str:
    return super().__repr__()

  def play(self):
    pass

  