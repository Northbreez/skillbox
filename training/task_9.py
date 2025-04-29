# Задача 1. Сумма чисел 2
# Пользователь вводит число N. Напишите функцию summa_n, которая принимает одно целое положительное число N
# и находит сумму всех чисел от 1 до N включительно.
# Функция вызывается два раза: сначала от числа N, а затем от полученной суммы.
# Пример работы программы:
# Введите число: 5
# Сумма от 1 до 5 = 15
# Сумма от 1 до 15 = 120
def summa_n(number):
    summa = 0
    for num in range(1, number + 1):
        summa += num
    return summa


user_number = int(input('Введите число: '))
first_number_sum = summa_n(user_number)
second_number_sum = summa_n(first_number_sum)

print(f'Сумма от 1 до {user_number} = {first_number_sum}')
print(f'Сумма от 1 до {first_number_sum} = {second_number_sum}')
