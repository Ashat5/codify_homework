#Ashat_Polvanov

# 1. Игра угадай число, в игре 3 уровня, на первом уровне у пользователя есть 1 попытка чтобы угадать число в диапазоне от 1 до 10,
# на втором уровне у него 3 попыток, диапазон чисел от 1 до 50, на третьем уровне у него 5 попыток, диапазон от 1 до 100,
# если он угадывает, то переходит на следующий уровень.

import random

def guess_number(attempts, end_of_range):
    users_attempts = 0
    number_to_guess = random.randint(1, end_of_range)
    while users_attempts != attempts:
        users_number = end_of_range + 1
        while users_number > end_of_range:
            try:
                users_number = int(input('Введите число от 1 до {}: '.format(end_of_range)))
                if users_number > end_of_range:
                    raise Exception ('Введите число из заданного диапазона!')
            except ValueError:
                print('Некорректный ввод!')
                users_number = end_of_range + 1
            except Exception as e:
                print(e)
                
        if users_number == number_to_guess:
            if end_of_range != 100:
                print('Поздравляем! Вы угадали число! Вы перешли в следующий раунд!')
                return True
            else:
                print('Поздравляем! Вы победитель!!!')
                return
        elif users_number != number_to_guess:
            users_attempts += 1
            remaining_attempts = attempts - users_attempts
            if remaining_attempts != 0:
                print('Неверный ответ! Оставшееся количество попыток: {}'.format(remaining_attempts))
            else:
                print('К сожалению вы проиграли!')
                return
                 
                
                
def main():
    print('*' * 120)
    print('''                                 ДОБРО ПОЖАЛОВАТЬ В ИГРУ "УГАДАЙ ЧИСЛО"!!!''')
    print('*' * 120)
    attempts = 1
    ends_of_range = [10, 50, 100]
    index = 0
    end_of_range = ends_of_range[index]
    result = True
    while result == True: 
        result = guess_number(attempts, end_of_range) 
        attempts += 2
        if attempts > 5:
            return
        index += 1
        end_of_range = ends_of_range[index]
        

main()