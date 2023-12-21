try:
    a = abs(int(input("Введите 1-е число: ")))
    b = abs(int(input("Введите 2-е число: ")))
except ValueError:
    print("ERROR")
    exit()
def nok(a, b, x):
    if x % a == 0 and x % b == 0:
        return x
    return nok(a, b, x+1)
print("НОК = ", nok(a, b, max(a, b)))