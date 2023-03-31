
cell = 3
field = [["-"] * cell for _ in range(cell)]

def show_field(f):
    print(" ", *[i for i in range(len(field))])# Нумерация столбцов
    for i in range(len(field)):
        print(str(i), *field[i])# Нумерация строк

def users_input(f):# если ее убрать то работает, но пока не прописали дальше
    while True:
        place = input("Введите координаты: ").split()
        if len(place) != 2 or not (place[0].isdigit() and place[1].isdigit()):
            print("Введены не целочисленные данные, укажите два занчения через пробел")
            continue
        x, y = map(int, place)
        if not 0 <= x < cell or not 0 <= y < cell:
            print(f"Числа должны быть в диапазоне от 0 до {cell-1}")#Возможно от 0 до 2 диапазон
            continue
        if f[y][x] != "-":
            print("Игровая клетка уже занята")
            continue
        break
    return x, y

def win(f, user):
    def check_line(a1, a2, a3, user):
        if a1 == a2 == a3 == user:
            return True
        return False
    for n in range(cell): # доработать ели больше клеток
        if check_line(f[n][0], f[n][1], f[n][2], user) or \
                check_line(f[0][n], f[1][n], f[2][n], user) or \
                check_line(f[0][0], f[1][1], f[2][2], user) or \
                check_line(f[2][0], f[1][1], f[0][2], user):
            return True
    return False

count = 0
while True:
    if count%2 == 0:
        user = "x"
    if count%2 != 0:
        user = "o"
    if count == cell**2:
        print("У Вас ничья! 🤝"
              "Игра закончена")
        break
    print(100 * '\n')
    show_field(field)
    x, y = users_input(field)
    field[y][x] = user
    if win(field, user):
        show_field(field)
        print(f"Поздравляю {user} выиграл!")
        break
    count += 1



