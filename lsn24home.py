"""Напишите функцию, которая получает
от пользователя два числа через input (),
 вызовите числа a и b, а затем вернете значение квадрата,
  деленное на b, создайте блок try-exc, который
вызывает исключение, если два значения заданы
По входной функции были не числа, а если значение
 b было равно нулю (делить на ноль нельзя). """


def func():
    a = input("Первое число: ")
    b = input("Второе число: ")
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print("Вы ввели не число!")

    try:
        rez = a ** 2 / b
        print(rez)
    except ZeroDivisionError:
        print("Делить на ноль нельзя!")


func()