from Plants.Plant import Plant


class Grass(Plant):
    def __init__(self, x, y, world):
        super().__init__(x, y, world, 'G', "Grass", 0, 0)