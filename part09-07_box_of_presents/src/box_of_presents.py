# WRITE YOUR SOLUTION HERE:
class Present:
  def __init__(self, name: str, weight: str):
    self.name = name
    self.weight = weight

  def __str__(self):
    return f"{self.name} ({self.weight} kg)"

class Box:
  def __init__(self):
    self.box_weight = 0

  def add_present(self, present: Present):
    self.box_weight += present.weight

  def total_weight(self):
    return self.box_weight