import random

def rock_paper_scissors():
    rps = {1: 'Камень', 2: 'Ножницы', 3: 'Бумага'}
    while True:
        user_answer = input('Выберите:\n1 - Камень\n2 - Ножницы\n3 - Бумага\nВаш выбор: ')
        if not user_answer.isdigit() or int(user_answer) not in rps:
            print('Ошибка ввода числа. Повторите.')
            continue
        user_answer = int(user_answer)
        bot_choice = random.choice(list(rps.keys()))
        print(f'Вы выбрали: {rps[user_answer]}, Бот выбрал: {rps[bot_choice]}')

        if user_answer == bot_choice:
            print('Ничья')
        elif (user_answer == 1 and bot_choice == 2) or \
             (user_answer == 2 and bot_choice == 3) or \
             (user_answer == 3 and bot_choice == 1):
            print('Вы выиграли!')
        else:
            print('Вы проиграли!')

        again = input('Хотите сыграть ещё раз? (да/нет): ').lower()
        if again != 'да':
            break

def guess_the_number():
    number_to_guess = random.randint(1, 10)
    while True:
        user_answer = input('Угадайте число от 1 до 10: ')
        if not user_answer.isdigit():
            print('Пожалуйста, введите число.')
            continue
        user_answer = int(user_answer)
        if user_answer < 1 or user_answer > 10:
            print('Число должно быть от 1 до 10.')
            continue

        if user_answer == number_to_guess:
            print('Поздравляем! Вы угадали число.')
            break
        else:
            print('Неправильно, попробуйте ещё раз.')

def main_menu():
    while True:
        print('Выберите игру:')
        print('1 - Камень, ножницы, бумага')
        print('2 - Угадай число')
        print('0 - Выход')
        choice = input('Ваш выбор: ')
        if choice == '1':
            rock_paper_scissors()
        elif choice == '2':
            guess_the_number()
        elif choice == '0':
            print('Выход из программы.')
            break
        else:
            print('Некорректный выбор, попробуйте снова.')

main_menu()