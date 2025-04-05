# Задача 3. Марсоход-2
# К роботу Валли планируют отправить «коллегу» Билли. Это первая высадка Билли на Марс,
# поэтому его тестируют в прямоугольном помещении размером 15 × 20 м.
# Марсоход высаживается в центре комнаты (в точке 8, 10), затем управление им передаётся оператору,
# то есть пользователю вашей программы.
# Программа спрашивает, в какую сторону оператор хочет направить робота:
# север (клавиша W), юг (клавиша S), запад (клавиша A) или восток (клавиша D).
# Оператор делает выбор, марсоход перемещается в эту сторону на один метр,
# а программа сообщает новую позицию робота.
# Если марсоход упёрся в стену, он не должен пытаться переместиться в сторону стены
# — в этом случае его позиция не меняется.
# Что нужно сделать
# Создайте программу для управления роботом Билли.

size_x = 15
size_y = 20
start_x = 8
start_y = 10
new_x = start_x
new_y = start_y
flag = True
count = 0
print((f"Марсоход находится на позиции {start_x, start_y}, введите команду: 'W', 'S', 'A'; 'D'"))
command = input()
while flag:
    if command == "w" or command == "W":
        if new_y >= 0 and new_y < size_y:
            new_y += 1
        elif new_y == size_y:
            new_y = size_y
    elif command == "s" or command == "S":
        if new_y > 0 and new_y <= size_y:
            new_y -= 1
        elif new_y == 0:
            new_y = 0
    elif command == "a" or command == "A":
        if new_x > 0 and new_x <= size_x:
            new_x -= 1
        elif new_x == 0:
            new_x = 0
    elif command == "d" or command == "D":
        if new_x >= 0 and new_x < size_x:
            new_x += 1
        elif new_x == size_x:
            new_x = size_x
    elif command == "start" or command == "Start":
        new_x = start_x
        new_y = start_y
    command= input((f"Марсоход находится на позиции {new_x, new_y}, введите команду: "))
    if new_x == 0 and new_y == 0 or new_x == size_x and new_y == size_y or new_x == 0:
        count +=1
    if count == 3:
        print(f"Человеки !!! I need help! Я застрял")
        break