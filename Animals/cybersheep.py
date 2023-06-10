from Animals.Animal import Animal
from Plants.SosmowskiHogweed import SosmowskiHogweed


class cybersheep(Animal):
    def __init__(self, x, y, world):
        super().__init__(x, y, world, 'c', "CyberSheep", 11, 4)
    def collision(self, victim, x, y):
        if victim.isStalked():
            self.x = x
            self.y = y
            self.world.SetPoint(self.x_priv, self.y_priv, None)
            self.world.SetPoint(x, y, self)
            self.world.AddComment(self.name + " killed " + victim.name)
            self.world.DeleteOrg(victim)
            victim.age = 0
        else:
            super().collision(victim, x, y)
    def action(self, range1):
        x = -1
        y = -1
        x_coo = []
        y_coo = []
        x_temp = self.x
        y_temp = self.y
        for i in self.world.organisms:
            if (isinstance(i, SosmowskiHogweed)):
                x_coo.append(i.x)
                y_coo.append(i.y)
        counter = self.world.height + self.world.width
        for i in range(len(x_coo)):
            tempx = x_coo[i] - self.x
            if tempx < 0:
                tempx *= -1
            tempy = y_coo[i] - self.y
            if tempy < 0:
                tempy *= -1
            path = tempx + tempy
            if path < counter:
                counter = path
                x = x_coo[i]
                y = y_coo[i]
        if x != -1:
            if x < self.x and x_temp-1 >= 0:
                x_temp -= 1
            elif x > self.x and x_temp+1 < self.world.width:
                x_temp += 1
            elif y < self.y and y_temp - 1 >= 0:
                y_temp -= 1
            elif y > self.y and y_temp + 1 < self.world.height:
                y_temp += 1
        else:
            super().action(range1)
            return

        self.x_priv = self.x
        self.y_priv = self.y
        if (self.world.GetPoint(x_temp, y_temp) != None):
            if self.world.GetPoint(x_temp, y_temp).TarczeAlzura(self):
                return
            if self.IsRunAway():
                return
            self.collision(self.world.GetPoint(x_temp, y_temp), x_temp, y_temp)
        else:
            self.x = x_temp
            self.y = y_temp
            self.world.SetPoint(self.x_priv, self.y_priv, None)
            self.world.SetPoint(x_temp, y_temp, self)

    def isKilledByHogweed(self):
        return False