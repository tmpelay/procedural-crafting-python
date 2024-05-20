from item.weapon.melee.sword.sword import Sword
from item.part.blade.blade import Blade
from item.part.grip.grip import Grip
from item.material.wood.wood import Wood

myWood = Wood()

mySwordBlade = Blade(myWood)
mySwordGrip = Grip(myWood)

mySword = Sword(1, "Excaliburg", 40, 110, mySwordBlade, mySwordGrip)
mySword.showInfo()