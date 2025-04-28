# Задача 3. Апгрейд калькулятора
# Степан использует калькулятор для расчёта суммы и разности чисел, но на работе ему требуются не только
# обычные арифметические действия. Он ничего не хочет делать вручную, поэтому решил немного расширить
# функциональность калькулятора.
# Что нужно сделать
# Напишите программу, запрашивающую у пользователя число и действие, которое нужно сделать с числом:
# вывести сумму его цифр, максимальную или минимальную цифру. Каждое действие оформите в виде отдельной функции,
# а основную программу зациклите.
# Запрошенные числа должны передаваться в функции суммы, максимума и минимума при помощи аргументов.

def processing_user_number():
    user_number = int(input('Введите целое число: '))
    choice = int(input('Введите номер действия:\n'
                       '1 - сумма цифр \n'
                       '2 - максимальная цифра \n'
                       '3 - минимальная цифра: '))

    def sum_user_number(num):
        sum = 0
        while num > 0:
            last_num = num % 10
            sum += last_num
            num //= 10
        print(sum)
        processing_user_number()
    def max_user_number(num):
        max_num = 0
        while num > 0:
            if num % 10 > max_num:
                max_num = num % 10
            num //= 10
        print(max_num)
        processing_user_number()
    def min_user_number(num):
        min_num = 9
        while num > 0:
            if num % 10 < min_num:
                min_num = num % 10
            num //= 10
        print(min_num)
        processing_user_number()

    if choice == 1:
        sum_user_number(user_number)
    elif choice == 2:
        max_user_number(user_number)
    elif choice == 3:
        min_user_number(user_number)
    else:
        print('Ошибка ввода.')
        print()
        processing_user_number()

processing_user_number()
