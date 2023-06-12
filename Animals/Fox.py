from Animals.Animal import Animal
import random

class Fox(Animal):
    def __init__(self, x, y, world):
        super().__init__(x, y, world, 'f', "Fox", 3, 7)

    def action(self, range):
        self.age += 1
        self.x_priv = self.x
        self.y_priv = self.y
        random_number = random.randint(0, self.world.CellNeighboursCounter - 1)
        x = self.x
        y = self.y
        counter = 0
        for i in (-1, 1):
            if 0 <= x + i < self.world.width and self.world.GetPoint(x + i, y) is not None and self.world.GetPoint(x + i, y).power > self.power:
                counter += 1
            if 0 <= y + i < self.world.height and self.world.GetPoint(x, y + i) is not None and self.world.GetPoint(x, y + i).power > self.power:
                counter += 1
        if (counter >= 4):
            return
        action = False
        while not action:
            if random_number == 0:
                if x + range >= self.world.width:
                    random_number = 1
                else:
                    x += range
                    action = True
            elif random_number == 1:
                if x - range < 0:
                    random_number = 2
                else:
                    x -= range
                    action = True
            elif random_number == 2:
                if y - range < 0:
                    random_number = 3
                else:
                    y -= range
                    action = True
            elif random_number == 3:
                if y + range >= self.world.height:
                    random_number = 1
                else:
                    y += range
                    action = True
            elif random_number == 4:
                if (y - range < 0 or x + range >= self.world.width):
                    random_number = 5
                else:
                    x += range
                    y -= range
                    action = True
            elif random_number == 5:
                if y + range >= self.world.height or x - range < 0:
                    random_number = 1
                else:
                    x -= range
                    y += range
                    action = True
            if self.world.GetPoint(x, y) != None and self.world.GetPoint(x, y).power > self.power:
                random_number = random.randint(0, self.world.CellNeighboursCounter)
                action = False

        if (self.world.GetPoint(x, y) != None):
            self.collision(self.world.GetPoint(x, y), x, y)
        else:
            self.x = x
            self.y = y
            self.world.SetPoint(self.x_priv, self.y_priv, None)
            self.world.SetPoint(x, y, self)
            self.world.AddComment(
                self.name + " moved from [" + str(self.x_priv) + ";" + str(self.y_priv) + "]" + " to [" + str(
                    x) + ";" + str(y) + "]")
    def NewOrganism(self, victim):
        x = []
        y = []
        self.world.FindPoints(self, x, y)
        self.world.FindPoints(victim, x, y)
        if (len(x) == 0):
            return None
        point = random.randint(0, len(x) - 1)
        x_temp = x[point]
        y_temp = y[point]
        a = Fox(x_temp, y_temp, self.world)
        return a