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

JA = Donkey("JA", "donkey", "morning", "straw", 334)
Black = Sheep("Black", "sheep", "afternoon", "hay", 123)
Billy = Goat("Billy", "goat", "midday", "pellets", 456)
Milkshake = Cow("Milkshake", "Cow", "morning", "grass", 765)
RedRum = Horse("RedRum", "horse", "midday", "apples", 678)

varmint_village.animals.extend([JA, Black, Billy, Milkshake, RedRum])

Noodles = Watersnake("Noodles", "watersnake", "fish", 198)
Zoe = Rattlesnake("Zoe", "rattlesnake", "rabbit", 444)
Snape = Cottonmouth("Snape", "cottonmouth", "salamander", 111)
Buttercup = Ratsnake("Buttercup", "ratsnake", "shrew", 222)
Sssssam = Copperhead("Sssssam", "copperhead", "mice", 555)

the_slither_inn.animals.extend([Noodles, Zoe, Snape, Buttercup, Sssssam])
 
Goldie = Goldfish("Goldie", "goldfish", "shelled peas", 989)
Romeo = RedFish("Romeo", "redfish", "mullet", 454)
Batman = BlueFish("Batman", "bluefish", "squid", 777)
Cleo = Catfish("Cleo", "catfish", "algae", 619)
Kiki = KoiFish("Kiki", "koi fish", "insects", 549)

critter_cove.animals.extend([Goldie, Romeo, Batman, Cleo, Kiki])

Black.feed()
Milkshake.feed()
Romeo.feed()

print(JA, Black, Billy, Milkshake, RedRum)
print(Noodles, Zoe, Snape, Buttercup, Sssssam)
print(Goldie, Romeo, Batman, Cleo, Kiki)

for animal in varmint_village.animals:
    print(f'You can find {animal.name} the {animal.species} in {varmint_village.attraction_name}')

for animal in the_slither_inn.animals:
    print(f'You can find {animal.name} the {animal.species} in {the_slither_inn.attraction_name}')

for animal in critter_cove.animals:
    print(f'You can find {animal.name} the {animal.species} in {critter_cove.attraction_name}')


Noodles.chip_num = 1234321

print('This is Noodle\'s chip_number: ', Noodles.chip_num)

print('The last critter added was: ', the_slither_inn.last_critter_added)
print('The last critter added was: ', critter_cove.last_critter_added)
print('The last critter added was: ', varmint_village.last_critter_added)