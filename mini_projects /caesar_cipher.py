def right(message, rotate, lang):
    res = ''
    if lang == "en":
        for i in message:
            rot = rotate
            if i.isalpha():
                if i.islower():
                    if ord(i) + rot > 122:
                        rot -= 122 - ord(i)
                        res += chr(96 + rot)
                        continue
                if i.isupper():
                    if ord(i) + rot > 90:
                        rot -= 90 - ord(i)
                        res += chr(64 + rot)
                        continue
                res += chr(ord(i) + rot)
            else:
                res += i
    else:
        for i in message:
            rot = rotate
            if i.isalpha():
                if i.islower():
                    if ord(i) + rot > 1103:
                        rot -= 1103 - ord(i)
                        res += chr(1072 + rot)
                        continue
                if i.isupper():
                    if ord(i) + rot > 1071:
                        rot -= 1071 - ord(i)
                        res += chr(1040 + rot)
                        continue
                res += chr(ord(i) + rot)
            else:
                res += i
    return res


def left(message, rotate, lang):
    res = ''
    if lang == "en":
        for i in message:
            rot = rotate
            if i.isalpha():
                if i.islower():
                    if ord(i) - rot < 97:
                        rot -= ord(i) - 97
                        res += chr(123 - rot)
                        continue
                if i.isupper():
                    if ord(i) - rot < 65:
                        rot -= ord(i) - 65
                        res += chr(91 - rot)
                        continue
                res += chr(ord(i) - rot)
            else:
                res += i
    else:
        for i in message:
            rot = rotate
            if i.isalpha():
                if i.islower():
                    if ord(i) - rot < 1072:
                        rot -= ord(i) - 1072
                        res += chr(1104 - rot)
                        continue
                if i.isupper():
                    if ord(i) - rot < 1040:
                        rot -= ord(i) - 1040
                        res += chr(1072 - rot)
                        continue
                res += chr(ord(i) - rot)
            else:
                res += i
    return res

print("\tЯзык: ru/en")
while True:
    n = input().lower()
    if n == "ru":
        lang = "ru"
        break
    if n == "en":
        lang = "en"
        break
    else:
        print("\tТакого ответа нет")

print("\tСообщение:")
message = input()

print("\tСдвиг:")
rot = int(input())

print("\tВлево/Вправо? Л/П")
while True:
    n = input()
    if n == "Л":
        res = left(message, rot, lang)
        break
    if n == "П":
        res = right(message, rot, lang)
        break
    else:
        print("\tТакого ответа нет")

print(res)
