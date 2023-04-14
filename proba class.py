from sea_fight import *
from random import choice, randint
class Sea:
    def __init__(self, empty, cell):
        self.map = [[empty] * cell for _ in range(cell)]
    def wright(self, x ,y):
    def __call__(self, *args, **kwargs):
        print(name)
        print(" ", *[i for i in range(len(self))])  # Нумерация столбцов
        for i in range(len(self)):
            print(str(i), *self[i])

class Random:
    x, y = randint(0, cell), randint(0, cell)
class Ship:
    def __init__(self, lenth, count):
        self.lenth = lenth
        self.count = count
        self.content = []
    # def __len__(self):
    #     if len(self) <= self.lenth:
    #         return len(self.content)
    # def __bool__(self):
    #     return self.content != []


ship3 = Ship(3, 1)
ship2 = Ship(2, 2)
ship1 = Ship(1, 4)

print(bool(ship3))