from Animals.Animal import Animal
class Wolf(Animal):
    def __init__(self, x, y, world):
        super().__init__(x, y, world, 'w', "Wolf", 9, 5)
