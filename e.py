try:
    n = int(input("Введетие десятичное представление: "))
except ValueError:
    print("ERROR")
    exit()
def dva(x, res):
    if len(res) == 7:
        if x // 2 != 0:
            print("ERROR")
            exit()
        return res
    res += str(x % 2)
    x //= 2
    return dva(x, res)
res = dva(abs(n), '')
if n >= 0:
    res = '0' + res[::-1]
else:
    res = '1' + res[::-1]
print(res)