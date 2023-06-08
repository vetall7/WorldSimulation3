from Plants.Plant import Plant


class Belladonna(Plant):
    def __init__(self, x, y, world):
        super().__init__(x, y, world, 'B', "Belladonna", 0, 0)