from random import *


def get_answer(ans):
    while True:
        if ans != "да" and ans != "нет":
            print("Неверный ответ!")
            continue
        else:
            return ans == "да"


def gen_password(amount, length, chars, not_inc):
    password_chars = "".join(
        [chars[i] for i in range(len(chars)) if not chars[i] in not_inc]
    )
    return ["".join(sample(password_chars, length)) for _ in range(amount)]


print("\tГенератор паролей")

print("\tСколько паролей создать?")
amount = int(input())

print("\tКакая будет длина?")
length = int(input())

print("\tВключать цифры? Да/Нет")
digits = "1234567890" if get_answer(input().lower()) else ""

print("\tВключать прописные буквы? Да/Нет")
upper_letters = (
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if get_answer(input().lower()) else ""
)

print("\tВключать строчные буквы? Да/Нет")
lower_letters = (
    "abcdefghijklmnopqrstuvwxyz" if get_answer(input().lower()) else ""
)

print("\tВключать символы? Да/Нет")
symbols = "!#$%&*+-=?@^_" if get_answer(input().lower()) else ""

print("\tИсключать неоднозначные символы (il1Lo0O)? Да/Нет")
not_inc = "" if get_answer(input().lower()) else "il1Lo0O"

print("\tХотите исключить какие-то отдельные символы? Да/Нет")
not_inc += input() if get_answer(input().lower()) else ""

chars = digits + upper_letters + lower_letters + symbols

print(gen_password(amount, length, chars, not_inc))
