try:
    b = int(input("Введите 0 член прогрессии: "))
    q = int(input("Введите разность прогрессии: "))
    n = int(input("Введите количество членов прогрессии: "))
    x = int(input("Введите номер члена прогрессии: "))
except ValueError:
    print("ERROR")
    exit()

if n == 0:
    print("Пустая последовательность")
    exit()
if x > n or x < 0 or n < 0:
    print("ERROR")
    exit()

def ari_prog(b, q, n, x, i):
    if i == x:
        return b
    i+=1
    b +=q
    return ari_prog(b, q, n, x, i)
print("n-й член = ", ari_prog(b, q, n, x, 0))