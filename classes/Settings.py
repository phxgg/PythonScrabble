class Settings:
  def __init__(self) -> None:
    self.computer_algorithm = 'min'
  
  def __repr__(self) -> str:
    return f'[ Settings ] Algorithm: {self.get_computer_algorithm()}'
  
  def get_computer_algorithm(self) -> str:
    return self.computer_algorithm

  def set_computer_algorithm(self, algorithm: str) -> None:
    self.computer_algorithm = algorithm
  