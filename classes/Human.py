from classes.Player import Player


class Human(Player):
  def __init__(self, name):
    super().__init__(name=name)

  def __repr__(self) -> str:
    pass

  