from Animals.Animal import Animal
class Human(Animal):
    def __init__(self, x, y, world):
        super().__init__(x, y, world, 'x', "Human", 5, 6)
        self.isSuperPower = False
        self.turn_counter = -10