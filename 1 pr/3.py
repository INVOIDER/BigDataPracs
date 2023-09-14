Sum = 0
SqrtSum = 0
while True:
    a = float(input())
    Sum += a
    SqrtSum += a * a
    if Sum == 0:
        print("Сумма квадратов: ", SqrtSum)
        break
