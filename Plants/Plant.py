from Main.Organism import Organism
import random

from Plants.Belladonna import Belladonna
from Plants.Dandelion import Dandelion
from Plants.Grass import Grass
from Plants.Guarana import Guarana
from Plants.SosmowskiHogweed import SosmowskiHogweed


class Plant(Organism):
    def __init__(self, x, y, world, sign, name, power, initiative):
        self._x = x
        self._y = y
        self._world = world
        self._sign = sign
        self._name = name
        self.power = power
        self.initiative = initiative

    def Action(self, range):
        rand_num = random.randint(20)
        if (rand_num == 0):
            new_plant = self.__NewPLant()
            if (new_plant != None):
                self.world.AddOrganism(new_plant)

    def __NewPLant(self):
        x = []
        y = []
        self.world.FindPoints(self, x, y)
        if len(x) == 0:
            return None
        point = random.randint(len(x))
        x_temp = x[point]
        y_temp = y[point]
        if (isinstance(self, Grass)):
            g = Grass(x_temp, y_temp, self.world)
            return g
        if (isinstance(self, Belladonna)):
            b = Belladonna(x_temp, y_temp, self.world)
            return b
        if (isinstance(self, Dandelion)):
            d = Dandelion(x_temp, y_temp, self.world)
            return d
        if (isinstance(self, Guarana)):
            g = Guarana(x_temp, y_temp, self.world)
            return g
        if (isinstance(self, SosmowskiHogweed)):
            s = SosmowskiHogweed(x_temp, y_temp, self.world)
            return s
        return None

    def Collision(self, victim, x, y):
        pass


