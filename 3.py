import random
N = random.randint(4, 30)
print("Всего: ", N)
i = 0
while (N > 0):
    if (i % 2 == 0):
        try:
            n_i = int(input("Введите кол-во камней (от 1 до 3): "))
        except ValueError:
            print("ERROR")
            exit()
        if (n_i > 3 or n_i < 1):
            print("Неправильное число")
            exit()
        N-=n_i
    else:
        print("Ходит бот")
        n_pc = random.randint(1, 3)
        N-=n_pc
    if (N < 0 or N == 0):
        if (i % 2 == 0):
            print("Вы выиграли!")
            break
        else:
            print("Вы проиграли!")
            break
    i+=1
    print("Осталось: ", N)
