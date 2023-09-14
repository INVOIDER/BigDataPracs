import math


# Площадь треугольника
def Triangle_Square(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


# Площадь прямоугольника
def SquareX2(a, b):
    return a * b


# Площадь круга
def Circle_Square(r):
    return 2 * math.pi * r * r


choice = -1
mas = {}
while choice != 0:
    if len(mas) == 3:
        print("Площади всех фигур: \n\n",mas)
        break
    print("Выберите фигуру: \n1.Треугольник\n2.Прямоугольник\n3.Круг")
    choice = int(input())
    if choice == 1:
        print("Введите 1ю сторону треуголньика: ")
        a = float(input())
        print("Введите 2ю сторону треуголньика: ")
        b = float(input())
        print("Введите 3ю сторону треуголньика: ")
        c = float(input())
        mas["Треугольник"] = Triangle_Square(a,b,c)
    elif choice==2:
        print("Введите 1ю сторону прямоугольника: ")
        a = float(input())
        print("Введите 2ю сторону прямоугольника: ")
        b = float(input())
        mas["Прямоугольник"] = SquareX2(a,b)
    elif choice==3:
        print("Введите радиус круга: ")
        r = float(input())
        mas["Круг"] = Circle_Square(r)

