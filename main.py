

class BoardException(Exception):
    pass

class BoardOutException(BoardException):
    def __str__(self):
        return "Вы пытаетесь выстрелить за доску!"

class BoardUsedException(BoardException):
    def __str__(self):
        return "Вы уже стреляли в эту клетку"

class BoardWrongShipException(BoardException):# исключение для позиционированя кораблей
    pass
class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y# сравниваем значения иксов и игриков как цифры: а не списки
    def __repr__(self): # для отладки - возвращает нам сразу Dot(x, y)
        return f"Dot({self.x}, {self.y})"
#

class Ship:
    def __init__(self, bow, l, o): #нос корабля, длина, ориентация
        self.bow = bow
        self.l = l
        self.o = o
        self.lives = l

    @property
    def dots(self):# проходим по всем точкам чтоы составить картину
        ship_dots = []
        for i in range(self.l):
            cur_x = self.bow.x
            cur_y = self.bow.y

            if self.o == 0:
                cur_x += i

            elif self.o == 1:
                cur_y += i

            ship_dots.append(Dot(cur_x, cur_y))

        return ship_dots

    def shooten(self, shot):# проверка на попадание
        return shot in self.dots

# s = Ship(Dot(1,0), 4, 0)
# print(s.dots)
# print(s.shooten(Dot(2, 0)))
class Board:
    def __init__(self, hid=False, size=6):
        self.size = size
        self.hid = hid
        self.count = 0
        self.field = [["O"] * size for _ in range(size)]
        self.busy = []
        self.ships = []
    def __str__(self):
        res = ""
        res += "  | 1 | 2 | 3 | 4 | 5 | 6 |"
        for i, row in enumerate(self.field):
            res += f"\n{i + 1} | " + " | ".join(row) + " |"

        if self.hid:
            res = res.replace("■", "O")
        return res

    def out(self, d):
        return not ((0 <= d.x < self.size) and (0 <= d.y < self.size))

print(Board())
