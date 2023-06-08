from Main.Organism import Organism


class Plant(Organism):
    def __init__(self, x, y, world, sign, name, power, initiative):
        self._x = x
        self._y = y
        self._world = world
        self._sign = sign
        self._name = name
        self.power = power
        self.initiative = initiative