import random
from Main.Organism import Organism
from Plants.Plant import Plant


class Animal(Organism):
    def __init__(self, x, y, world, sign, name, power, initiative):
        super().__init__()
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
        self.age += 1
        self.x_priv = self.x
        self.y_priv = self.y
        random_number = random.randint(0, self.world.CellNeighboursCounter-1)
        x = self.x
        y = self.y
        while True:
            if random_number == 0:
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
                if (y - range < 0 or x + range >= self.world.width):
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
            if self.world.GetPoint(x, y).TarczeAlzura(self):
                return
            if self.IsRunAway():
                return
            self.collision(self.world.GetPoint(x, y), x, y)
        else:
            self.x = x
            self.y = y
            self.world.SetPoint(self.x_priv, self.y_priv, None)
            self.world.SetPoint(x, y, self)
            #self.world.AddComment(self.name + " moved from [" + str(self.x_priv) + ";" + str(self.y_priv) + "]" + " to [" + str(x) + ";" + str(y) + "]")

    def collision(self, victim, x, y):
        if (victim.age == 0):
            return
        if (victim.sign == self._sign):
            temp = self.__NewOrganism(victim)
            if temp != None:
                self.world.AddOrganism(temp)
                self.world.AddComment(temp.name + "was born")
        elif (self.power > victim.power):
            if (victim.DidDeflectedAttack(self)):
                return
            self.x = x
            self.y = y
            self.world.SetPoint(self.x_priv, self.y_priv, None)
            self.world.SetPoint(x, y, self)
            self.world.AddComment(self.name + " killed " + victim.name)
            if (isinstance(victim, Plant)):
                victim.collision(self, x, y)
            self.world.DeleteOrg(victim)
            victim.age = 0
        elif(self.power <= victim.power):
            self.world.AddComment(victim.name + " killed " + self.name)
            self.world.SetPoint(self.x_priv, self.y_priv, None)
            self.world.DeleteOrg(self)

    def __NewOrganism(self, victim):
        from Animals.Wolf import Wolf
        from Animals.Fox import Fox
        from Animals.Turtle import Turtle
        from Animals.Antelope import Antelope
        from Animals.Sheep import Sheep
        from Animals.cybersheep import cybersheep
        x = []
        y = []
        self.world.FindPoints(self, x, y)
        self.world.FindPoints(victim, x, y)
        if (len(x) == 0):
            return None
        point = random.randint(0, len(x)-1)
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
        if (isinstance(self, cybersheep)):
            a = cybersheep(x_temp, y_temp, self.world)
            return a
        return None

    def isKilledByHogweed(self):
        return True