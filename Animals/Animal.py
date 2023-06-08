import random

from Wolf import Wolf
from Fox import Fox
from Turtle import Turtle
from Antelope import Antelope
from Sheep import Sheep
from Main.Organism import Organism
from Plants.Plant import Plant


class Animal(Organism):
    def __init__(self, x, y, world, sign, name, power, initiative):
        self._x = x
        self._y = y
        self._world = world
        self._sign = sign
        self._name = name
        self.power = power
        self.initiative = initiative
    def IsRunAway(self):
        return False

    def action(self, range):
        self._age += 1
        self._x_priv = self.x
        self._y_priv = self.y
        random_number = random.randint(self.world.CellNeighboursCounter)
        x = self.x
        y = self.y
        while True:
            if random_number == 0 :
                if x + range >= self.world.width:
                    random_number = 1
                else:
                    x += range
                    break
            elif random_number == 1:
                if x - range < 0:
                    random_number = 2
                else:
                    x -= range
                    break
            elif random_number == 2:
                if y - range < 0:
                    random_number = 3
                else:
                    y -= range
                    break
            elif random_number == 3:
                if y + range >= self.world.height:
                    random_number = 1
                else:
                    y += range
                    break
            elif random_number == 4:
                if (y - range < 0 or x + range >= self.width):
                    random_number = 5
                else:
                    x += range
                    y -= range
                    break
            elif random_number == 5:
                if y + range >= self.world.height or x - range < 0:
                    random_number = 1
                else:
                    x -= range
                    y += range
                    break

        if (self.world.GetPoint(x, y) != None):
            if self.IsRunAway():
                return
            self.Collision(self.world.GetPoint(x, y), x, y)
        else:
            self.x = x
            self.y = y
            self.world.SetPoint(self._x_priv, self._y_priv, None)
            self.world.SetPoint(x, y, self)

    def Collision(self, victim, x, y):
        if (victim.age == 0):
            return
        if (victim.sign == self._sign):
            temp = self.__NewOrganism(victim)
            if temp != None:
                self.world.AddOrganism(temp)
        elif (self.power > victim.power):
            self.x = x
            self.y = y
            self.world.SetPoint(self._x_priv, self._y_priv, None)
            self.world.SetPoint(x, y, self)
            if (isinstance(victim, Plant)) :
                victim.Collision(self, x, y)
            self.world.DeleteOrg(victim)
        elif(self.power <= victim.power):
            self.world.SetPoint(self.x_priv, self._y_priv, None)
            self.world.DeleteOrg(self)



    def __NewOrganism(self, victim):
        x = []
        y = []
        self.world.FindPoints(self, x, y)
        self.world.FindPoints(victim, x, y)
        if (len(x) == 0):
            return None
        point = random.randint(len(x))
        x_temp = x[point]
        y_temp = y[point]

        if (isinstance(self, Wolf)):
            w = Wolf(x_temp, y_temp, self.world)
            return w
        if (isinstance(self, Sheep)):
            s = Sheep(x_temp, y_temp, self.world)
            return s
        if (isinstance(self, Fox)):
            f = Fox(x_temp, y_temp, self.world)
            return f
        if (isinstance(self, Turtle)):
            t = Turtle(x_temp, y_temp, self.world)
            return t
        if (isinstance(self, Antelope)):
            a = Antelope(x_temp, y_temp, self.world)
            return a
        return None
