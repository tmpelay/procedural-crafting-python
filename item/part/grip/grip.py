from item.part.part import Part

class Grip(Part):
    def __init__(self, material):
        self.volume = 0.00075
        self.material = material
        self.weight = round(material.density * self.volume, 2)