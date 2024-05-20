from item.part.part import Part

class Blade(Part):
    def __init__(self, material):
        self.volume = 0.001
        self.material = material
        self.weight = round(material.density * self.volume, 2)