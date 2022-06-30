from classes.Player import Player


class Computer(Player):
  def __init__(self):
    super().__init__(name='Computer')

  def __repr__(self) -> str:
    pass