from Animals.Animal import Animal


class Sheep(Animal):
    def __init__(self, x, y, world):
        super().__init__(x, y, world, 's', "Sheep", 4, 4)
