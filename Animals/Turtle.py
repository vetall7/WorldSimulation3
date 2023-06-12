import random

from Animals.Animal import Animal


class Turtle(Animal):
    def __init__(self, x, y, world):
        super().__init__(x, y, world, 't', "Turtle", 2, 1)

    def DidDeflectedAttack(self, attacker):
        if (attacker.power < 5):
            attacker.x = attacker.x_priv
            attacker.y = attacker.y_priv
            self.world.AddComment("Turtle deflected attack")
            return True
        return False
    def action(self, range):
        rand_num = random.randint(0,4)
        if (rand_num == 0):
            super().action(range)
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
        a = Turtle(x_temp, y_temp, self.world)
        return a