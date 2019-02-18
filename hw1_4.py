"""
4. Написать программу, которая генерирует в указанных пользователем границах:

    случайное целое число;
    случайное вещественное число;
    случайный символ.

Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ
от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита
от 'a' до 'f' включительно.

"""

import random


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def negative_detect(value):
    if value[0] == '-':
        return -1, value[1:]
    else:
        return 1, value


def generate_random_int(value):
    y = input("Введите второе целое число, не равное первому \n")

    multiplier, y = negative_detect(y)

    if y.isdigit():
        y = int(y) * multiplier
        if y == value:
            print("Числа совпадают. Повторите ввод с самого начала")
            return 1
        else:
            if value < y:
                print(random.randint(value, y))
            if value > y:
                print(random.randint(y, value))
            return 0

    else:
        print("Введено не целое число. Повторите ввод с самого начала")
        return 1


def generate_random_alpha(value):
    y = input("Введите второй символ, не равное первому \n")

    multiplier, y = negative_detect(y)

    if y.isalpha() and y.__len__() == 1:
        if multiplier == -1:
            print("Некорректный ввод. Повторите с самого начала")
            return 1
        else:
            y = y[0]
            if y == value:
                print("Символы совпадают. Повторите ввод с самого начала")
                return 1
            else:
                if ord(value) < ord(y):
                    print(chr(random.randint(ord(value), ord(y))))
                if ord(value) > ord(y):
                    print(chr(random.randint(ord(y), ord(value))))
                return 0
    else:
        print("Некорректный ввод. Повторите с самого начала")
        return 1


def generate_random_float(value):
    y = input("Введите второе действительное число, не равное первому \n")

    multiplier, y = negative_detect(y)

    if isfloat(y):
        y = float(y)
        if y == value:
            print("Числа совпадают. Повторите ввод с самого начала")
            return 1
        else:
            if value < y:
                print(random.uniform(value, y))
            if value > y:
                print(random.uniform(y, value))
            return 0
    else:
        print("Некорректный ввод. Повторите с самого начала")
        return 1


def main():
    flag = 1
    
    while flag:

        x = input("Введите первое число или символ из диапазона.\n")

        multiplier, x = negative_detect(x)

        if x.isalpha() and x.__len__() == 1:
            if multiplier == -1:
                print("Некорректный ввод. Повторите")
                flag = 1
            else:
                print("Введен символ")
                print(x[0])

                flag = generate_random_alpha(x[0])

        elif x.isdigit():
            print("Введено целое число")
            print(int(x) * multiplier)
            flag = generate_random_int(int(x) * multiplier)
        elif isfloat(x):
            print("Введено действительное число")
            print(float(x) * multiplier)
            flag = generate_random_float(float(x) * multiplier)
        else:
            print("Ввод не верный. Повторите")


if __name__ == "__main__":
    main()
