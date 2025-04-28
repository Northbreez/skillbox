# Задача 5. Недоделка
# Вы пришли на работу в компанию по разработке игр, целевая аудитория — дети и их родители.
# У предыдущего программиста было задание сделать две игры в одном приложении,
# чтобы пользователь мог выбирать одну из них.
# Однако программист, на место которого вы пришли, перед увольнением не успел выполнить эту задачу и
# оставил только небольшой шаблон проекта.
#
# Правила игры «Камень, ножницы, бумага»: программа запрашивает у пользователя строку и выводит,
# победил он или проиграл. Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.
#
# Правила игры «Угадай число»: программа запрашивает у пользователя число до тех пор,
# пока он не угадает загаданное.
#
# Что нужно сделать
# Используя этот шаблон проекта, реализуйте игры «Камень, ножницы, бумага» и «Угадай число».
import random


def user_name_printout(user_name):
    print(f'Привет, {user_name}')
user = input("Введите ваше имя: ")
user_name_printout(user)

def game_continue_rps():
    game_continue = int(input(f'Повторим?\n'
                              f'1 - Да\n'
                              f'2 - Нет\n'))
    if game_continue == 1:
        rock_paper_scissors()
    else:
        main_menu()

def game_continue_qtn():
    game_continue = int(input(f'Повторим?\n'
                              f'1 - Да\n'
                              f'2 - Нет\n'))
    if game_continue == 1:
        guess_the_number()
    else:
        main_menu()

def rock_paper_scissors():  # Игра «Камень, ножницы, бумага»`
    user_answer = int(input('Выберите:\n'
                            '1 - Камень \n'
                            '2 - Ножницы \n'
                            '3 - Бумага \n'
                            'Твой ответ: '))
    rps = {1: 'Камень', 2: 'Ножницы', 3: 'Бумага'}
    res = random.choice(list(rps.keys()))
    if 0 >= user_answer or user_answer > 3:
        print('Ошибка ввода числа. Повторите')
        game_continue_rps()
    else:
        if (user_answer == 1 and res == 2) or (user_answer == 2 and res == 3) or (user_answer == 3 and res == 1):
            print(f'Ты выйграл. Бот выбрал - {rps.get(res)}')
            game_continue_rps()
        elif user_answer == res:
            print(f'Ничья')
            game_continue_rps()
        else:
            print(f'Ты проиграл. Бот выбрал - {rps.get(res)}')
            game_continue_rps()

def guess_the_number():  # Игра «Угадай число»
    user_answer = int(input('Выберите число от 1 до 10:\n'
                            'Твой ответ: '))
    if 0 >= user_answer or user_answer > 10:
        print('Ошибка ввода числа. Повторите')
        game_continue_qtn()
    else:
        res = random.randint(1, 10)
        if user_answer == res:
            print(f'Ты выйграл. Бот выбрал - {res}')
            game_continue_qtn()
        else:
            print(f'Ты проиграл. Бот выбрал - {res}')
            game_continue_qtn()

def main_menu():  # Главное меню игры
    choice = int(input(f'{user}, выберите игру:\n'
                       '1 - Камень, ножницы, бумага \n'
                       '2 - Угадай число \n'))
    if choice == 1:
        rock_paper_scissors()
    elif choice == 2:
        guess_the_number()
main_menu()