def to_ten(num, base):
    res = 0
    num = list(num)

    if base > 10:
        for i in range(len(num)):
            if num[i] in "ABCDEF":
                num[i] = ord(chr(num[i]) - 55)
    
    i = len(num) - 1
    for j in num:
        res += int(j) * base**i
        i -= 1
    return res

def from_ten(num, base):
    res = ''
    while num > 0:
        s = num % base
        if s > 9:
            s = chr(ord('A') + s % 10)
        res += str(s)
        num //= base
    return res[::-1]

while True:
    print("\tЧисло")
    num = input()

    print("\tСистема")
    base = int(input())

    print("\tИз 10 или в 10? 1/2")
    s = input()
    
    if s == "1":
        print(from_ten(int(num), base))
        break
    if s == "2":
        print(to_ten(num, base))
        break
    else:
        print("\tТакого ответа нет!")
