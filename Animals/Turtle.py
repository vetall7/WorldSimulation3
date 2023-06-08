from Animals.Animal import Animal


class Turtle(Animal):
    def __init__(self, x, y, world):
        super().__init__(x, y, world, 't', "Turtle", 2, 1)
