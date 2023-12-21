try:
    b = int(input("Введите 0 член прогрессии: "))
    q = float(input("Введите знаменатель прогрессии: "))
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
def geo_prog(b, q, n, x, i, s):
    if i == x:
        return s
    return geo_prog(b*q, q, n, x, i+1, s+(b*q))
print("Сумма = ", geo_prog(b, q, n, x, 0, b))