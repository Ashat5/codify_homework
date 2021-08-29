#Ashat_Polvanov

# Напишите программу которая позволяет пользователю:
# 1. Записать какой-то текст в файл 
# 2. Найти записанный текст в файле по дате, либо по содержимому в ней.

import sys
import os
import datetime

users_input = 0
while users_input != 3:
    try:
        users_input = int(input('''
        1. Записать текст в файл.
        2. Найти записанный текст в файле по дате, либо по содержимому в нем.
        3. Выйти из приложения.
        Выберите опцию: '''))
        if users_input not in range(1,4):
            raise Exception('Выберите опцию из имеющихся!')
    except ValueError:
        print('Некорректный ввод!')
    except Exception as e:
        print(e)
    if users_input == 1:
        users_text = input('Введите текст: ')
        date = str(datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S '))
        with open(os.path.join(sys.path[0], 'users_file.txt' ), 'a') as file:
            file.write(date + '%s' % users_text + '\n')
        
        
    if users_input == 2:
        finding_object = input('Введите дату или текст который хотите найти: ')
        with open(os.path.join(sys.path[0], 'users_file.txt' ), 'r') as file:
            for line in file:
                if finding_object in line:
                    print('Ваш текст найден: ', line)
