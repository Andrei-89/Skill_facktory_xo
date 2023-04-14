from termcolor import cprint

miss = "."
hit = "+"
empty = "-"
cell = 6
null = " "


def field(cell):
    return [[empty] * cell for _ in range(cell)]  # функция создания поля


def show_field(f, name):
    print(name)
    print(" ", *[i for i in range(len(f))])  # Нумерация столбцов
    for i in range(len(f)):
        cprint(str(i), *f[i])  # Нумерация строк


field_1 = field(cell)
field_2 = field(cell)


# условие заполнения поля на количество кораблей и отступы
# def ship_import(f):
#     while True:
#     # сначало ранмодино водятся трехтрубные корабли и резервируется поле вокруг них
#     # вводятся двутрубные две штуки
#     # вводятся однострубные 4 штуки
#         if f[y][x] == empty:
#             for i in range(2):
#                 for j in range(2):
#                     f[i-1][j-1] = miss
#             f[y][x] = hit
#             continue
# if f[y][x] == miss and (f[y][x-1] == hit or f[y][x+1] == hit or f[y-1][x] == hit or f[y+1][x] == hit):

#             # и если вокруг соседних крестиков тоже точки то далее
#             # если вокруг крестиков есть крестики и f[y] = второго кретика f[y]
#             # или если f[x] = второго кретика f[x]
#             # и если 3трубных все еще нет в поле то f[y][x] = hit
#             # если 2-x двухтрубных нет в поле f[y][x] = hit
#             # если четырех 1трубных нет в поле f[y][x] = hit
#
#         break
#     return f[y][x] = hit
def users_input(f):
    place = input("Введите координаты: ").split()
    if len(place) != 2 or not (place[0].isdigit() and place[1].isdigit()):
        print("Введены не целочисленные данные, укажите два занчения через пробел")
    x, y = map(int, place)
    return x, y


def win(f, x, y):
    for i in range(2):
        if f[y][x + i] == f[y][x + i + 1] == f[y][x + i + 2] == hit or f[y + i][x] == f[y + i + 1][x] == f[y + i + 2][
            x] == hit:
            continue
        if (y + i + 2) < cell and (x + i + 2) < cell:
            continue
    for j in range(1):
        for i in range(1):
            if f[y + j][x + i] == f[y + j][x + i + 1] == hit or f[y + i][x + j] == f[y + i + 1][x + j] == hit:
                continue
            if (y + i) < cell and (x + i) < cell and (x + j) < cell and (y + j) < cell:
                continue
    return False


def margin(f, x, y):
    f[y][x] = hit
    for i in range(3):
        for j in range(3):
            if 0 <= (y + i - 1) < (cell) and 0 <= (x + j - 1) < (cell):
                if f[y + i - 1][x + j - 1] != hit:
                    f[y + i - 1][x + j - 1] = miss


def margin_ending(f, x, y):
    f[y][x] = 2
    for i in range(3):
        for j in range(3):
            if 0 <= (y + i - 1) < (cell) and 0 <= (x + j - 1) < (cell):
                if f[y + i - 1][x + j - 1] != hit:
                    f[y + i - 1][x + j - 1] = null


def test(f, x, y):
    while True:
        if f[y][x] == miss and (f[y][x - 1] == hit or f[y][x + 1] == hit or f[y - 1][x] == hit or f[y + 1][x] == hit):
            for i in range(1):
                if f[y][x] == f[y][x + i] == f[y][x + i + 1] == hit or f[y][x] == f[y][x - i] == f[y][
                    x - i - 1] == hit or f[y][x] == f[y - i][x] == f[y - i - 1][x] == hit or f[y][x] == f[y + i][x] == \
                        f[y + i + 1][x] == hit:
                    margin_ending(f, x, y)
                else:
                    margin_ending(f, x, y)
        if f[y][x] == empty:
            margin(f, x, y)

        break
    return


show_field(field_1, "Player")
show_field(field_2, "Random")
while True:
    x, y = users_input(field_1)
    test(field_1, x, y)
    print(show_field(field_1, "Player"))

    # if win(field_1, x, y):
    #     print("Ура! Оно Работает!")
