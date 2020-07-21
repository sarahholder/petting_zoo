class PettingZoo:
    def __init__(self, name):
      self.attraction_name = name
      self.description = "cute and fuzzy critters to cuddle"
      self.animals = list()
    
    @property
    def last_critter_added(self):
        return self.animals[-1]


class SnakePit:
    def __init__(self, name):
      self.attraction_name = name
      self.description = "stupendous snakes of all sizes"
      self.animals = list()

    @property
    def last_critter_added(self):
        return self.animals[-1]

class Wetlands:
    def __init__(self, name):
      self.attraction_name = name
      self.description = "wet bar-- need I say more"
      self.animals = list()

    @property
    def last_critter_added(self):
        return self.animals[-1]

