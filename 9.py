x1 = 100
y1 = 100
r1 = 40

x2 = 110
y2 = 100
r2 = 30

root = turtle.Turtle()  # root - экземпляр класса

root.penup()
root.goto(x1, y1)
root.pendown()
root.circle(r1)

root.penup()
root.goto(x2, y2)
root.pendown()
root.circle(r2)

d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

if (d > r2 + r1):
    print("Окружности лежат одна вне другой, не касаясь")

elif (d == r1 + r2):
    print("Окружности имеют внешнее касание")

elif (d < r1 + r2 and d > abs(r1 - r2)):
    print("Окружности пересекаются")

elif (d == abs(r1 - r2)):
    print("Окружности имеют внутреннее касание")

elif (d < abs(r1 - r2)):
    print("Одна окружность лежит внутри другой, не касаясь")

input()