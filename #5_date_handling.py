#Ashat_Polvanov

# 1. Написать программу с помощью которой пользователь, по выбору, может посмотреть
# - текущее число
# - месяц
# - год
# - время
# - полную дату и время в формате '%m/%d/%Y %H:%M:%S'


import datetime

def view_datetime_function():
    ''' Функция с помощью которой пользователь, по выбору, может посмотреть текущее число, месяц, год, время, полную дату'''
    print('Здравствуйте, вы в программе которая позволит вам посмотреть текущую дату или точное время!')
    users_input = None
    while users_input != 6: 
        try:
            users_input = int(input('''
        Вы можете посмотреть:
        1. Текущее число
        2. Месяц
        3.Год
        4.Время
        5.Полную дату и время
        6.Выйти из программы
        Введите цифру: '''))
            if users_input not in range(1,7):
                raise Exception ('Выберите опцию из имеющихся!')
        except ValueError:
            print('Некорректный ввод!')
        except Exception as e:
            print (e)

        if users_input == 1:
            print('Текущее число: ', datetime.datetime.now().day)
        elif users_input == 2:
            print('Текущий месяц: ', datetime.datetime.now().strftime('%B'))
        elif users_input == 3:
            print('Текущий год: ', datetime.datetime.now().year)
        elif users_input == 4:
            print('Текущее время: ', datetime.datetime.now().strftime('%H:%M:%S'))
        elif users_input == 5:
            print('Дата и время: ', datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S'))

view_datetime_function()

        