from Plants.Plant import Plant


class Dandelion(Plant):
    def __init__(self, x, y, world):
        super().__init__(x, y, world, 'D', "Dandelion", 0, 0)
    def action(self, range):
        super().action(range)
        super().action(range)
        super().action(range)