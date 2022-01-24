print('Добро пожаловать в игру \n "Крестики / нолики"')
print('Для осуществления хода, введите координаты \n от 0 до 2 включительно')

area = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]


def pole():
    print(f"   0 1 2")
    for i in range(3):
        print(f' {i} {area[i][0]} {area[i][1]} {area[i][2]}')


def xod():
    while True:
        crd = input(" ход\n").split()

        if len(crd) != 2:
            print("нужно ввести 2 координаты")
            continue

        a, b = crd

        if not (a.isdigit()) or not(b.isdigit()):
            print("нужно ввести числа")
            continue

        a, b = int(a), int(b)

        if 0 > a or a > 2 or 0 > b or b > 2:
            print("неверные координаты")
            continue

        if area[a][b] != " ":
            print("координаты заняты")
            continue

        return a, b

def wincheck():
        wincrds = [
            ((0, 0), (0, 1), (0, 2)),
            ((1, 0), (1, 1), (1, 2)),
            ((2, 0), (2, 1), (2, 2)),
            ((0, 2), (1, 1), (2, 0)),
            ((0, 0), (1, 1), (2, 2)),
            ((0, 0), (1, 0), (2, 0)),
            ((0, 1), (1, 1), (2, 1)),
            ((0, 2), (1, 2), (2, 2))
        ]
        for crd in wincrds:
            symbols = []
            for c in crd:
                symbols.append(area[c[0]][c[1]])
            if symbols == ["X", "X", "X"]:
                print("Победил крестик")
                return True
            if symbols == ["O", "O", "O"]:
                print("Победил нолик")
                return True
        return False




num = 0
while True:
    num += 1

    pole()

    if num % 2 == 1:
        print("ход крестика")
    else:
        print("ход нолика")

    a, b = xod()

    if num % 2 == 1:
        area[a][b] = "X"
    else:
        area[a][b] = "O"


    if wincheck():
        break

    if num == 9:
        print("ничья")
        break
