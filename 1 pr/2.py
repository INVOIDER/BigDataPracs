def Sum(a, b):
    return a + b


def Sub(a, b):
    return a - b


def Mult(a, b):
    return a * b


def Div(a, b):
    return a / b


def Pow(a, b):
    res = a
    for i in range(1, b):
        res = res * a
    return res


def Div_int(a, b):
    return int(a / b)


def Abs(a):
    return abs(a)


print("Калькулятор\n")

print("Введите 1 число: ")
a = float(input())
print("Введите знак: ")
z = input()
if z == 'abs':
    print('|', a, '|=', Abs(a))
else:
    print("Введите 2е число: ")
    b = float(input())

    if z == '+':
        print(a, "+", b, "=", Sum(a, b))
    elif z == '-':
        print(a, "-", b, "=", Sub(a, b))
    elif z == '*':
        print(a, "*", b, "=", Mult(a, b))
    elif z == '/':
        print(a, "/", b, "=", Div(a, b))
    elif z == '//':
        print(a, "//", b, "=", Div_int(a, b))
    elif z == '**' or z == 'pow':
        print(a, "*", b, "=", Pow(a, b))
