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