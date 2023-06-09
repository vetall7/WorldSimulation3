import random

from Animals.Animal import Animal


class Antelope(Animal):
    def __init__(self, x, y, world):
        super().__init__(x, y, world, 'a', "Antelope", 4, 4)
    def action(self, range):
        super().action(2)
    def IsRunAway(self):
        rand = random.randint(0,10)
        if rand < 5:
            if self.x - 2 > 0 and self.world.GetPoint(self.x-2, self.y) == None:
                self.world.SetPoint(self.x, self.y, None)
                self.x -= 2
                self.world.SetPoint(self.x, self.y, self)
            elif self.x + 2 < self.world.width and self.world.GetPoint(self.x+2, self.y) == None:
                self.world.SetPoint(self.x, self.y, None)
                self.x += 2
                self.world.SetPoint(self.x, self.y, self)
            elif self.y - 2 > 0 and self.world.GetPoint(self.x, self.y-2) == None:
                self.world.SetPoint(self.x, self.y, None)
                self.y -= 2
                self.world.SetPoint(self.x, self.y, self)
            elif self.y + 2 < self.world.height and self.world.GetPoint( self.x, self.y+2) == None:
                self.world.SetPoint(self.x, self.y, None)
                self.y += 2
                self.world.SetPoint(self.x, self.y, self)
            self.world.AddComment("Antelope run away [" + str(self.x) + ";" + str(self.y) + "]" )
            return True
        return False