from datetime import date

class Animal:
    def __init__(self, name, species, food, chip_num):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.food = food
        self.__chip_num = chip_num

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f'{self.name} is a {self.species}.\n'

    @property
    def chip_num(self):
        return self.__chip_num

    @chip_num.setter
    def chip_num(self, new_chip_num):
        pass
        # raise RuntimeError("Can't touch this!")


#outdoor corral (walking)
class Donkey(Animal): 
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True

    # def __init__(self, name, species, shift, food):
    #   self.name = name
    #   self.species = species
    #   self.date_added = date.today()
    #   self.walking = True
    #   self.shift = shift
    #   self.food = food

    # def feed(self):
    #   print(f'{self.name} was fed on {date.today().strftime("%m/%d/%Y")}')
      
    # def __str__(self):
    #   return f"This animal is named {self.name}, it is a {self.species} and it was added on {self.date_added} and it is {bool(self.walking)} that it walks and it is available to pet during the {self.shift} shift.\n"

class Sheep(Animal): 
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)        
        self.shift = shift
        self.walking = True

    def feed(self):
        print(f'on {date.today()}, {self.name} had "Baa Baa black sheep" sung to it so it would eat its {self.food}')

class Goat(Animal): 
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)        
        self.shift = shift
        self.walking = True

class Cow(Animal): 
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True
    
    def feed(self):
        print(f'on {date.today()}, {self.name} wants to dance while having the song "Milkshake" sung to ease digestion of {self.food}')

class Horse(Animal): 
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True

#glass tank(slithering)
class Watersnake(Animal): 
    def __init__(self, name, species, food, chip_num):
      super().__init__(name, species, food, chip_num)
      self.slithering = True

class Rattlesnake(Animal): 
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True


class Cottonmouth(Animal): 
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True
 
class Ratsnake(Animal): 
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True

class Copperhead(Animal): 
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True

#goldfish pond(swimming)

class Goldfish(Animal): 
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True

class RedFish(Animal): 
    def __init__(self, name, species, food, chip_num):
      super().__init__(name, species, food, chip_num)
      self.swimming = True

    def feed(self):
        print(f'on {date.today()}, {self.name} had the book "One Fish, Two Fish, Red Fish, Blue Fish" read to it so it could relish in its {self.food}')

class BlueFish(Animal): 
    def __init__(self, name, species, food, chip_num):
      super().__init__(name, species, food, chip_num)
      self.swimming = True

class Catfish(Animal): 
    def __init__(self, name, species, food, chip_num):
      super().__init__(name, species, food, chip_num)
      self.swimming = True

class KoiFish(Animal): 
    def __init__(self, name, species, food, chip_num):
      super().__init__(name, species, food, chip_num)
      self.swimming = True

# for prop, value in JA.__dict__.items():
    #  print(f'{prop}:\n{value}\n')


