from weapon.melee.melee import Melee

class Sword(Melee):
    def __init__(self, hands, name, weight, damage, length):
        super().__init__(hands)
        self.name = name
        self.weight = weight
        self.damage = damage
        self.lenght = length
        
    def showInfo(self):
        print(f"the {self.name} is used with {self.hands} hands")
        print(f"The {self.name} weight is: {self.weight}kg")
        print(f"The {self.name} damage is: {self.damage}dp")
        print(f"The {self.name} length is: {self.lenght}cm")
    