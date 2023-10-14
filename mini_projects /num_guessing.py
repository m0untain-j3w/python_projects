from random import *


def is_valid(x, a, b):
    if not x.isdigit():
        return False
    else:
        return a <= int(x) <= b


def num_guess(r_num):
    global lim
    global tries
    print("\tЯ загадал число, угадайте его")
    while True:
        n = input()
        if not is_valid(n, 1, lim):
            print(f"\tНужно число от 1 до {lim}")
            continue
        n = int(n)
        if n == r_num:
            print("\tВы угадали число!")
            print(f"\tКоличество попыток: {tries}")
            break
        if n < r_num:
            print("\tЧисло меньше загаданного")
            tries += 1
        else:
            print("\tЧисло больше загаданного")
            tries += 1


# Продолжение/Конец игры
def continue_game():
    print("\tПродолжаем? Да/Нет")
    while True:
        ans = input().lower()
        if ans != "да" and ans != "нет":
            print("\tНеверный ответ!")
            continue
        return ans == "да"


# Игра
def game():
    global tries
    global lim
    while True:
        print("\tУгадываем число от 1 до ___", end=" ")
        lim = int(input())
        tries = 1
        r_num = randint(1, lim)
        num_guess(r_num)
        if continue_game():
            continue
        else:
            break


game()
