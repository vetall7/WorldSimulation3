import random

from Animals.Animal import Animal
from Main.directions import Direction
class Human(Animal):
    def __init__(self, x, y, world):
        super().__init__(x, y, world, 'x', "Human", 5, 6)
        self.__isSuperPower = False
        self.__turn_counter = -10
        self.__direction = Direction.TURN_NONE

    @property
    def super_power(self):
        return self.__isSuperPower
    @super_power.setter
    def super_power(self, value):
        self.__isSuperPower = value

    @property
    def turn_count(self):
        return self.__turn_counter

    @turn_count.setter
    def turn_count(self, value):
        self.__turn_counter = value

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, value):
        self.__direction = value

    def TarczeAlzura(self, attacker):
        if (not self.__isSuperPower):
            return False
        x_points = []
        y_points = []
        self.world.SetPoint(attacker.x, attacker.y, None)
        self.world.FindPoints(self, x_points, y_points)
        if (len(x_points) == 0):
            return False
        rand = random.randint(0, len(x_points)-1)
        attacker.x = x_points[rand]
        attacker.y = y_points[rand]
        self.world.SetPoint(attacker.x, attacker.y, attacker)
        self.world.AddComment("Human scared away " + attacker.name)
        return True

    def action(self, range):
        self.age += 1
        self.x_priv = self.x
        self.y_priv = self.y
        x = self.x
        y = self.y

        if self.direction == Direction.TURN_DOWN and self.y + 1 < self.world.height:
            y += 1
        if self.direction == Direction.TURN_UP and self.y - 1 >= 0:
            y -= 1
        if self.direction == Direction.TURN_LEFT and self.x - 1 >= 0:
            x -= 1
        if self.direction == Direction.TURN_RIGHT and self.x + 1 < self.world.width:
            x += 1
        if self.direction == Direction.TURN_UP_RIGHT and self.x + 1 < self.world.width and self.y - 1 >= 0:
            x += 1
            y -= 1
        if self.direction == Direction.TURN_DOWN_LEFT and self.x - 1 >= 0 and self.y + 1 < self.world.height:
            x -= 1
            y += 1
        if (self.__direction == Direction.TURN_SUPER):
            if self.world.turn <= self.__turn_counter + 10:
                self.world.AddComment("SUPERPOWER CANNOT BE ACTIVATED")
                print ("SUPERPOWER CANNOT BE ACTIVATED")
            else:
                self.__turn_counter = self.world.turn
                self.world.AddComment("ACTIVATED SUPERPOWER")
                print ("ACTIVATED SUPERPOWER")
                self.__isSuperPower = True

        if self.__isSuperPower:
            if self.world.turn == self.__turn_counter + 5:
                self.__isSuperPower = False
                self.world.AddComment("SUPERPOWER DEACTIVATED")
                print ("SUPERPOWER DEACTIVATED")

        if (self.world.GetPoint(x, y) != None):
            if self.IsRunAway():
                return
            self.collision(self.world.GetPoint(x, y), x, y)
        else:
            self.x = x
            self.y = y
            self.world.SetPoint(self.x_priv, self.y_priv, None)
            self.world.SetPoint(x, y, self)
            self.world.AddComment(
                self.name + " moved from [" + str(self.x_priv) + ";" + str(self.y_priv) + "]" + " to [" + str(
                    x) + ";" + str(y) + "]")
