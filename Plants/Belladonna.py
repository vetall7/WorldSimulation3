from Plants.Plant import Plant


class Belladonna(Plant):
    def __init__(self, x, y, world):
        super().__init__(x, y, world, 'B', "Belladonna", 0, 0)
    def collision(self, attacker, x, y):
        self.world.AddComment(self.name + " killed " + attacker.name)
        self.world.SetPoint(x, y, None)
        self.world.DeleteOrg(attacker)