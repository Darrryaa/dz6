cell = input("Введите координаты клетки (Пример: a1): ")

column = ord(cell[0]) - ord('b')
row = int(cell[1])

if (column + row) % 2 == 0:
    print("Черный")
else:
    print("Белый")