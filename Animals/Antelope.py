from Animals.Animal import Animal


class Antelope(Animal):
    def __init__(self, x, y, world):
        super().__init__(x, y, world, 'a', "Antelope", 4, 4)
