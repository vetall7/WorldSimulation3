from Plants.Plant import Plant


class SosmowskiHogweed(Plant):
    def __init__(self, x, y, world):
        super().__init__(x, y, world, 'h', "SosmowskiHogweed", 0, 0)