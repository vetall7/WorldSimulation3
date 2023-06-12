from Animals.Animal import Animal
import random

class Sheep(Animal):
    def __init__(self, x, y, world):
        super().__init__(x, y, world, 's', "Sheep", 4, 4)

    def NewOrganism(self, victim):
        x = []
        y = []
        self.world.FindPoints(self, x, y)
        self.world.FindPoints(victim, x, y)
        if (len(x) == 0):
            return None
        point = random.randint(0, len(x) - 1)
        x_temp = x[point]
        y_temp = y[point]
        a = Sheep(x_temp, y_temp, self.world)
        return a