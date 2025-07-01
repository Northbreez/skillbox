# Задача 3. Апгрейд калькулятора
# Степан использует калькулятор для расчёта суммы и разности чисел, но на работе ему требуются не только
# обычные арифметические действия. Он ничего не хочет делать вручную, поэтому решил немного расширить
# функциональность калькулятора.
# Что нужно сделать
# Напишите программу, запрашивающую у пользователя число и действие, которое нужно сделать с числом:
# вывести сумму его цифр, максимальную или минимальную цифру. Каждое действие оформите в виде отдельной функции,
# а основную программу зациклите.
# Запрошенные числа должны передаваться в функции суммы, максимума и минимума при помощи аргументов.
from random import choice


def sum_user_number(num):
    sum_num = 0
    while num > 0:
        last_num = num % 10
        sum_num += last_num
        num //= 10
    return sum_num


def max_user_number(num):
    max_num = -1
    while num > 0:
        digit = num % 10
        if digit > max_num:
            max_num = digit
        num //= 10
    return max_num


def min_user_number(num):
    min_num = 9
    while num > 0:
        digit = num % 10
        if  digit < min_num:
            min_num = digit
        num //= 10
    return min_num


user_number = int(input('Введите целое число: '))
while choice != 0:
    choice = int(input('Введите номер действия:\n'
                       '1 - сумма цифр \n'
                       '2 - максимальная цифра \n'
                       '3 - минимальная цифра \n'
                       '0 - выход: '))
    if choice == 1:
        print(f'Сумма цифр: {sum_user_number(user_number)}')
        print()
    elif choice == 2:
        print(f'Максимальная цифра: {max_user_number(user_number)}')
        print()
    elif choice == 3:
        print(f'Минимальная цифра: {min_user_number(user_number)}')
        print()
    elif choice == 0:
        print('Выход из программы')
        break
    else:
        print('Ошибка ввода.')
        print()
