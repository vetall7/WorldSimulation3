from abc import ABC, abstractmethod
from abc import ABC, abstractmethod
from Main.Organism import Organism
from Animals.Animal import Animal
from Main.directions import Direction
from Plants.Plant import Plant

class World(ABC):
    def __init__(self, height, width):
        self._height = height
        self._width = width
        self._turn = 0
        self._organisms = []
        self._comments = []
        self._board = [[None] * width for _ in range(height)]
        self._human = None
        self._CellNeighboursCounter = 4
        self._cellSize = 50

    def AddComment(self, comment):
        self._comments.append(comment)

    @property
    def turn(self):
        return self._turn

    @turn.setter
    def turn(self, value):
        self._turn = value

    @property
    def human(self):
        return self._human

    @human.setter
    def human(self, value):
        self._human = value

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def CellNeighboursCounter(self):
        return self._CellNeighboursCounter

    def get_org_counter(self):
        return len(self._organisms)

    @property
    def organisms(self):
        return self._organisms
    def SetPoint(self, x, y, organism):
        self._board[y][x] = organism
    def AddOrganism(self, organism):
        self._organisms.append(organism)
        self.SetPoint(organism.x, organism.y, organism)
    def DeleteOrg(self,target_organism):
        self._organisms = [organism for organism in self._organisms if organism is not target_organism]

    @abstractmethod
    def DrawWorld(self, generate):
        pass


    def GetPoint(self, x, y):
        return self._board[y][x]

    @abstractmethod
    def FindPoints(self, org, x, y):
        pass


    def Turn(self):
        self._comments.clear()
        self.turn += 1
        for i in self._organisms:
            if i.age == 0:
                i.age = 1

        sorted_organisms = sorted(self.organisms, key=lambda o: (-o.initiative, o.age))

        for i in sorted_organisms:
            if i.age != 0:
                i.action(1)
    @abstractmethod
    def FindNeighbours(self, org, x, y):
        pass
    def _NewOrganism(self, name, x, y):
        from Animals.Fox import Fox
        from Animals.Antelope import Antelope
        from Animals.Sheep import Sheep
        from Animals.Turtle import Turtle
        from Animals.Wolf import Wolf
        from Plants.Belladonna import Belladonna
        from Plants.Dandelion import Dandelion
        from Plants.Grass import Grass
        from Plants.Guarana import Guarana
        from Plants.SosmowskiHogweed import SosmowskiHogweed


        if name == "Fox":
            f = Fox(x, y, self)
            return f
        if name == "Antelope":
            a = Antelope(x, y, self)
            return a
        if name == "Sheep":
            s = Sheep(x, y, self)
            return s
        if name == "Turtle":
            t = Turtle(x, y, self)
            return t
        if name == "Wolf":
            w = Wolf(x, y, self)
            return w
        if name == "Belladonna":
            b = Belladonna(x, y, self)
            return b
        if name == "Dandelion":
            d = Dandelion(x, y, self)
            return d
        if name == "Grass":
            g = Grass(x, y, self)
            return g
        if name == "Guarana":
            g = Guarana(x, y, self)
            return g
        if name == "SosmowskiHogweed":
            s = SosmowskiHogweed(x, y, self)
            return s