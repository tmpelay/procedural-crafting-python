from item.weapon.melee.sword.sword import Sword
from item.part.blade.blade import Blade
from item.part.grip.grip import Grip

mySwordBlade = Blade(1)
mySwordGrip = Grip(0.5)

mySword = Sword(1, "Excaliburg", 40, 110, mySwordBlade, mySwordGrip)
mySword.showInfo()