from Animals.Animal import Animal


class Fox(Animal):
    def __init__(self, x, y, world):
        super().__init__(x, y, world, 'f', "Fox", 3, 7)
