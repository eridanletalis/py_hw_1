"""
3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.

"""


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def main():
    global flag
    flag = 1
    coords = [0.0, 0.0, 0.0, 0.0]

    while flag:

        x = input("Введите координаты двух точек в формате x1 y1 x2 y2\n")
        a = x.split(" ")
        if a.__len__() != 4:
            print("Формат ввода не верный. Вводите числа, разделяя их пробелом")
            flag = 1
        else:
            for i, check in enumerate(a):
                negative = 1
                if check[0] == '-':
                    check = check[1:]
                    negative = -1
                if check.isnumeric() or isfloat(check):
                    coords[i] = (negative * float(check))
                    flag = 0
                else:
                    flag = 1
                    print("Один из введённых элементов не является числом")
                    coords = [0.0, 0.0, 0.0, 0.0]
                    break

    if coords[0] == coords[2] and coords[1] == coords[3]:
        print("Введённые точки совпадают, вывод уравнения линии невозможен")
    elif coords[1] == coords[3]:
        print("Линия параллельная оси абсцисс, её уравнение y = %f" % coords[1])
    elif coords[0] == coords[2]:
        print("Линия параллельная оси ординат, её уравнение x = %f" % coords[2])
    else:
        print("Уравнение прямой: y = %fx + %f" % ((coords[3]-coords[1])/(coords[2]-coords[0]), \
                                                (coords[1] - coords[0]*(coords[3]-coords[1])/(coords[2]-coords[0]))))

if __name__ == "__main__":
    main()
