from animals import Donkey
from animals import Sheep
from animals import Goat
from animals import Cow
from animals import Horse
from animals import Watersnake
from animals import Rattlesnake
from animals import Cottonmouth
from animals import Ratsnake
from animals import Copperhead
from animals import Goldfish
from animals import RedFish
from animals import BlueFish
from animals import Catfish
from animals import KoiFish

from attractions import PettingZoo
from attractions import SnakePit
from attractions import Wetlands

varmint_village = PettingZoo("Varmint Village")
the_slither_inn = SnakePit("The Slither Inn")
critter_cove = Wetlands("Critter Cove")

JA = Donkey("JA", "donkey", "morning", "straw")
Black = Sheep("Black", "sheep", "afternoon", "hay")
Billy = Goat("Billy", "goat", "midday", "pellets")
Milkshake = Cow("Milkshake", "Cow", "morning", "grass")
RedRum = Horse("RedRum", "horse", "midday", "apples")

varmint_village.animals.extend([JA, Black, Billy, Milkshake, RedRum])

Noodles = Watersnake("Noodles", "watersnake")
Zoe = Rattlesnake("Zoe", "rattlesnake")
Snape = Cottonmouth("Snape", "cottonmouth")
Buttercup = Ratsnake("Buttercup", "ratsnake")
Sssssam = Copperhead("Sssssam", "copperhead")

the_slither_inn.animals.extend([Noodles, Zoe, Snape, Buttercup, Sssssam])

Goldie = Goldfish("Goldie", "goldfish")
Romeo = RedFish("Romeo", "red fish")
Batman = BlueFish("Batman", "blue fish")
Cleo = Catfish("Cleo", "catfish")
Kiki = KoiFish("Kiki", "koi fish")

critter_cove.animals.extend([Goldie, Romeo, Batman, Cleo, Kiki])

print(JA, JA.feed(), Black, Black.feed(), Billy, Billy.feed(), Milkshake, Milkshake.feed(), RedRum, RedRum.feed())
print(Noodles, Zoe, Snape, Buttercup, Sssssam)
print(Goldie, Romeo, Batman, Cleo, Kiki)

for animal in varmint_village.animals:
    print(f'You can find {animal.name} the {animal.species} in {varmint_village.attraction_name}')

for animal in the_slither_inn.animals:
    print(f'You can find {animal.name} the {animal.species} in {the_slither_inn.attraction_name}')

for animal in critter_cove.animals:
    print(f'You can find {animal.name} the {animal.species} in {critter_cove.attraction_name}')


