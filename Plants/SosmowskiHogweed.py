from Animals.Animal import Animal
from Plants.Plant import Plant


class SosmowskiHogweed(Plant):
    def __init__(self, x, y, world):
        super().__init__(x, y, world, 'h', "SosmowskiHogweed", 0, 0)
    def action(self, range2):
        x_coo = []
        y_coo = []
        self.world.FindNeighbours(self, x_coo, y_coo)
        if len(x_coo) == 0:
            return
        for i in range(len(x_coo)):
            if (
                    self.world.GetPoint(x_coo[i], y_coo[i]) is not None
                    and isinstance(self.world.GetPoint(x_coo[i], y_coo[i]), Animal)
                    and self.world.GetPoint(x_coo[i], y_coo[i]).isKilledByHogweed()
            ):
                self.world.AddComment(
                    "SosmowskiHogweed killed " + self.world.GetPoint(x_coo[i], y_coo[i]).name
                )
                self.world.DeleteOrg(self.world.GetPoint(x_coo[i], y_coo[i]))
                self.world.SetPoint(x_coo[i], y_coo[i], None)
    def isStalked(self):
        return True