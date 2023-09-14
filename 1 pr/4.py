print("Введите N: ")
N = int(input())
mas = []
for i in range(0, N):
    for j in range(0, i):
        mas.append(i)
        print(len(mas))
        if len(mas) == N:
            print("Массив: ", mas)
            exit()

