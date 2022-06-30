from classes.Player import Player


class Computer(Player):
  def __init__(self):
    super().__init__(name='Η/Υ')

  def __repr__(self) -> str:
    return f'Computer({self.name})'

  def play(self):
    pass

  