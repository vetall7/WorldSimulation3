from Plants.Plant import Plant


class Guarana(Plant):
    def __init__(self, x, y, world):
        super().__init__(x, y, world, 'g', "Guarana", 0, 0)
    def collision(self, attacker, x, y):
        attacker.power_increase(3)