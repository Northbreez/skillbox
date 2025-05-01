# Число наоборот
# Что нужно сделать
# Пользователь вводит два числа: N и K.
# Напишите программу, которая переворачивает каждое из введённых чисел,
# то есть записывает эти числа в обратном порядке.
# Пример
# Введите первое число: 102
# Введите второе число: 123
# Первое число наоборот: 201
# Второе число наоборот: 321

def reverse_num(num):
    reverse_word = ''
    while num > 0:
        last_num = num % 10
        last_num = str(last_num)
        num //= 10
        reverse_word += last_num
    reverse_num = int(reverse_word)
    return reverse_num


def result(first, second):
    print(f'Первое число наоборот: {reverse_num(first)}')
    print(f'Второе число наоборот: {reverse_num(second)}')


first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
result(first_number, second_number)
