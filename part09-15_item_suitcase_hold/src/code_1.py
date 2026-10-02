class Item:
  def __init__(self, name, weight):
    self.__name = name
    self.__weight = weight

  def __str__(self):
    return f"{self.__name} ({self.__weight} kg)"

  def name(self):
    return self.__name

  def weight(self):
    return self.__weight

class Suitcase:
  def __init__(self, max_weight):
    self.__max_weight = max_weight
    self.items = []

  def add_item(self, item):
    current_weight = 0
    for i in self.items:
      current_weight += i.weight()
    if current_weight + item.weight() <= self.__max_weight:
      self.items.append(item)

  def __str__(self):
    current_weight = 0
    for i in self.items:
      current_weight += i.weight()
    if len(self.items) == 1:
      return f"{len(self.items)} item ({current_weight} kg)"
    else:
      return f"{len(self.items)} items ({current_weight} kg)"

  def print_items(self):
    for item in self.items:
      print(f"{item.name()} ({item.weight()} kg)")

  def weight(self):
    current_weight = 0
    for lista_tavara in self.items:
      current_weight += lista_tavara.weight()
    return current_weight

  def heaviest_item(self):
    max_weight = 0
    max_item = None
    for item in self.items:
      if item.weight() > max_weight:
        max_weight = item.weight()
        max_item = item
    return max_item

class CargoHold:
  def __init__(self, maximum_weight):
    self.__maximum_weight = maximum_weight
    self.__suitcases = []

  def add_suitcase(self,suitcase):
    current_weight = 0
    for item in self.__suitcases:
      current_weight += item.weight()
    if current_weight + suitcase.weight() <= self.__maximum_weight:
      self.__suitcases.append(suitcase)
      self.__maximum_weight -= suitcase.weight()

  def __str__(self):
    if len(self.__suitcases) == 1:
      return f"{len(self.__suitcases)} suitcase, space for {self.__maximum_weight} kg"
    else:
      return f"{len(self.__suitcases)} suitcases, space for {self.__maximum_weight} kg"

  def print_items(self):
    for suitcase in self.__suitcases:
      for item in suitcase.items:
        print(f"{item.name()} ({item.weight()} kg)")