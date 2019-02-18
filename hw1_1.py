"""
1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

"""


def main():
    global number
    flag = 1
    
    while flag:

        x = input("Введите трёхзначное целое число.\n")

        if x.isdigit() != 1:
            print("Введено не число или число не целое")
            flag = 1
        else:
            number = int(x)
            if number < 100 or number > 1000:
                print("Введёное число не трёзначное")
                flag = 1
            else:
                flag = 0

    x1 = int(number/100)
    x2 = int((number-x1*100)/10)
    x3 = number - x1*100 - x2*10

    print("Сумма: %d"%(x1 + x2 + x3))
    print("Произведение: %d"%(x1 * x2 * x3))


if __name__ == "__main__":
    main()
