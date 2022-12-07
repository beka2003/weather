import sys
from math import sqrt


# функ. проверяющая является ли введеное значение цифрой
def isNum(string):
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


arr = []
while True:
    a = input('введите число: ')
    if a == "":
        break

    # Проверка является ли введеное число цифрой
    if not isNum(a):
        print('Вы ввели не число')
        sys.exit()

    # Записываем в массив число
    else:
        arr.append(a)


# Проверка сколько введено значений
if len(arr) <= 2:
    print('вы ввели меньше 3 значений')
    sys.exit()


# Переводим строку в число
result = [float(arg) for arg in arr]
result.sort()


# Получаем 3 самых больших числа
x = result[-1]
y = result[-2]
z = result[-3]


# Мат. функция по расчету
def func(x, y, z):
    p = (x + y + z) / 2
    s = sqrt((p * (p - x) * (p - y) * (p - z)))
    print(s)

# Проверяем является ли 3 полученных числа полож. и то что они не равны 0
if x > 0 and y > 0 and z > 0:
    if x + y > z and x + z > y and z + y > x:
        func(x, y, z)
    else:
        print('Такого треугольника не существует')
else:
    print('Такого треугольника не существует')
