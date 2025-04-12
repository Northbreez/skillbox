# Задание 5. Наибольшая сумма цифр
# Пользователь вводит N чисел. Среди натуральных чисел, которые он указал, найдите наибольшее по сумме цифр.
# Выведите на экран это число и сумму его цифр.
# Пример
# Введите количество чисел: 3
# Введите число: 5
# Введите число: 98
# Введите число: 453
# Число 98 имеет максимальную сумму цифр: 17

start_num = int(input('Введите количество чисел: '))
total_sum = 0
top_num = 0
sum_number = 0
for num in range(start_num):
    number = int(input('Введите число: '))
    ex_number = number
    while number != 0:
        last_num = number % 10
        number = number // 10
        sum_number += last_num
        if sum_number > total_sum:
            total_sum = sum_number
            top_num = ex_number
    sum_number = 0
print(f'Число {top_num} имеет максимальную сумму цифр: {total_sum}')