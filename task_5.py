num = int(input("Введите число от 1 до 10: "))
count = 0
while num <= 0 or num > 10:
    print("Вы ввели число, не соответствующее диапазону от 1 до 10")
    num = int(input("Введите число от 1 до 10: "))
input_num = int(input("Введите число: "))
count += 1
while input_num != num:
    if input_num > num:
        print("Число больше, чем нужно. Попробуйте ещё раз!")
    elif input_num < num:
        print("Число меньше, чем нужно. Попробуйте ещё раз!")
    count += 1
    input_num = int(input("Введите число: "))
print(f'Вы угадали! Число попыток: {count}')