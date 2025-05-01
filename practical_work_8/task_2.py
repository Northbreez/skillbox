# Функция максимума
# Юра пишет различные полезные функции для Python, чтобы остальным программистам стало проще работать.
# Он захотел написать функцию, которая будет находить максимум из перечисленных чисел.
# Функция для нахождения максимума из двух чисел у него уже есть.
# Юра задумался: может быть, её можно использовать для нахождения максимума уже от трёх чисел?
# Что нужно сделать
# Помогите Юре написать программу, которая находит максимум из трёх чисел.
# Для этого используйте только функцию нахождения максимума из двух чисел.
# По итогу в программе должны быть реализованы две функции:
# maximum_of_two — функция принимает два числа и возвращает одно (наибольшее из двух);
# maximum_of_three — функция принимает три числа и возвращает одно (наибольшее из трёх);
# при этом она должна использовать для сравнений первую функцию maximum_of_two.
def maximum_of_two(first, second):
    maximum = first
    if maximum < second:
        maximum = second
    return maximum

def start_two_numbers():
    first_number = int(input('Введите первое число: '))
    second_number = int(input('Введите второе число: '))
    max_of_two = maximum_of_two(first_number, second_number)
    print(f'Максимальное число из введенных: {max_of_two}')

def start_three_numbers():
    first_number = int(input('Введите первое число: '))
    second_number = int(input('Введите второе число: '))
    three_number = int(input('Введите третье число: '))
    max_of_two = maximum_of_two(first_number, second_number)
    max_of_three = maximum_of_two(max_of_two, three_number)
    print(f'Максимальное число из введенных: {max_of_three}')

def start():
    menu_num = int(input('Сколько чисел хотите сравнить? 2 или 3: '))
    if menu_num == 2:
        start_two_numbers()
    elif menu_num == 3:
        start_three_numbers()
    else:
        print('Не верный запрос сравнения чисел. Повторите еще.')
        start()
start()