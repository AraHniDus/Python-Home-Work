number = int(input('Введите число от 1 до 7 - '))

def checkNumber(num):
    if 6 <= num <= 7:
        print("Да")
    elif 0 < num < 6:
        print("Нет")
    else:
        print("Число вне пределов  дней недели")

num = number
checkNumber(num)