import random
from Animals.Human import Human
from Animals.Wolf import Wolf
from Animals.Fox import Fox
from Animals.Sheep import Sheep
from Animals.Turtle import Turtle
from Animals.Antelope import Antelope

from Plants.Belladonna import Belladonna
from Plants.Dandelion import Dandelion
from Plants.Grass import Grass
from Plants.Guarana import Guarana
from Plants.SosmowskiHogweed import SosmowskiHogweed
class WorldGenerator():
    def __init__(self, world):
        self.__world = world
    def __CoordinateGenerate(self, x, y, ocupied):
        x[0] = random.randint(0, self.__world.width-1)
        y[0] = random.randint(0, self.__world.height-1)
        for i in range(0, len(ocupied), 2):
            if ocupied[i] == x[0] and ocupied[i + 1] == y[0]:
                x[0] = random.randint(0, self.__world.width-1)
                y[0] = random.randint(0, self.__world.height-1)
                i = -2
        ocupied.append(x[0])
        ocupied.append(y[0])

    def Generate(self):
        x = [1]
        y = [1]
        ocupied = []
        counter = (self.__world.height * self.__world.width / 4) * 2
        if counter < 20:
            counter += 9
        self.__CoordinateGenerate(x, y, ocupied)
        human = Human(x[0], y[0], self.__world)
        self.__world.AddOrganism(human)
        self.__world.human = human
        for i in range (0, int(counter/20)):
            self.__CoordinateGenerate(x, y, ocupied)
            wolf = Wolf(x[0], y[0], self.__world)
            self.__world.AddOrganism(wolf)

            self.__CoordinateGenerate(x, y, ocupied)
            fox = Fox(x[0], y[0], self.__world)
            self.__world.AddOrganism(fox)

            self.__CoordinateGenerate(x, y, ocupied)
            turtle = Turtle(x[0], y[0], self.__world)
            self.__world.AddOrganism(turtle)

            self.__CoordinateGenerate(x, y, ocupied)
            antelope = Antelope(x[0], y[0], self.__world)
            self.__world.AddOrganism(antelope)

            self.__CoordinateGenerate(x, y, ocupied)
            sheep = Sheep(x[0], y[0], self.__world)
            self.__world.AddOrganism(sheep)

            self.__CoordinateGenerate(x, y, ocupied)
            belladonna = Belladonna(x[0], y[0], self.__world)
            self.__world.AddOrganism(belladonna)

            self.__CoordinateGenerate(x, y, ocupied)
            dandelion = Dandelion(x[0], y[0], self.__world)
            self.__world.AddOrganism(dandelion)

            self.__CoordinateGenerate(x, y, ocupied)
            grass = Grass(x[0], y[0], self.__world)
            self.__world.AddOrganism(grass)

            self.__CoordinateGenerate(x, y, ocupied)
            guarana = Guarana(x[0], y[0], self.__world)
            self.__world.AddOrganism(guarana)

            self.__CoordinateGenerate(x, y, ocupied)
            sosmowskihogweed = SosmowskiHogweed(x[0], y[0], self.__world)
            self.__world.AddOrganism(sosmowskihogweed)
