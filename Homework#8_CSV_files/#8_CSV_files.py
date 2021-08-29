#Ashat_Polvanov

# 1. Напишите программу которая спрашивает ФИО, телефон пользователя и 
# записывает их в файл, в виде словаря, обработайте возможные ошибки.
# 2. Расширьте возможность программы (1) добавив поиск по ФИО, телефону.
# 3. Расширьте возможность программы (1) и (2) добавив удаление данных по ФИО, телефону.
import csv
import os
import sys



numbers = ['1','2','3','4','5','6','7','8','9','0']
my_database = []

users_input = 0
while users_input != 4:
    users_input = 0
    try:
        users_input = int(input('''
        1. Записать данные в файл.
        2. Найти данные по Ф.И.О. или номеру телефона.
        3. Удалить данные по Ф.И.О. или номеру телефона.
        4. Выйти из приложения.
        Выберите опцию: '''))
        if users_input not in range(1,5):
            raise Exception('Выберите опцию из имеющихся!')
    except ValueError:
        print('Некорректный ввод!')
    except Exception as e:
        print(e)

    if users_input == 1:
        result = False
        def proofreading_user_input(object):
            try:
                if not object:
                    raise Exception ('Вы ничего не ввели!')
                else:
                    for i in object:
                        if i in numbers:
                            raise Exception ('Ф.И.О не должны содержать цифры!')
            except Exception as e:
                print(e)
                object = None
                return object
            except Exception as e:
                print (e)
            return object

        while result == False:
            users_name = input('Введите ваше имя: ')
            users_name = proofreading_user_input(users_name)
            if users_name :
                while result == False:
                    users_last_name = input('Введите вашу фамилию: ')
                    users_last_name = proofreading_user_input(users_last_name)
                    if users_last_name:
                        while result == False:
                            users_middle_name = input('Введите ваше отчество: ')
                            users_middle_name = proofreading_user_input(users_middle_name)
                            if users_middle_name:
                                result = True


        users_phone = ''
        while type(users_phone) != int:
            try:
                users_phone = int(input('Введите ваш номер телефона: '))
            except ValueError:
                print('Некорректный ввод!')



        my_database.append({'name' : users_name, 'last_name' : users_last_name, 'middle_name' : users_middle_name,\
        'phone' : users_phone})


        FILE_NAME = os.path.join(sys.path[0], 'user_data.txt')
        with open(FILE_NAME, 'w', encoding='utf-8') as file:
            writer = csv.DictWriter(file, my_database[0].keys())
            writer.writeheader()
            writer.writerows(my_database)
    
    if users_input == 2:
        if len(my_database) > 0:
            finding_object = input('Введите что-то из Ф.И.О или номер телефона для поиска данных: ')
            with open(FILE_NAME, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for line in file:
                    if finding_object in line:
                        print('Ваши данные найдены: ', line)
                    else:
                        ('Ваши данные не найдены!')
        else:
            print('В файле пока нет никаких данных!')

    if users_input == 3:
        if len(my_database) > 0:
            finding_object_to_del = input('Введите что-то из Ф.И.О или номер телефона для удаления найденных данных: ')
            with open(FILE_NAME, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for line in file:
                    if finding_object_to_del in line:
                        print('Данные найдены: ', line)
                        finding_object_to_del = line
                deletion_confirmation = input('''
                Если хотите удалить эти данные введите "да", если не хотите нажмите любую клавишу.
                Ваш ввод: ''')
                deletion_confirmation = deletion_confirmation.lower()
                if deletion_confirmation == 'да':
                    lines = list()
                    with open(FILE_NAME, 'r', encoding='utf-8') as file:
                        reader = csv.reader(file)
                        for row in file:
                            if row != finding_object_to_del:
                                if row != '\n':
                                    edit_row = row.replace('\n', '')
                                    lines.append(edit_row)
                        lines = lines[1: -1]



                    with open(FILE_NAME, 'w', encoding='utf-8') as file:
                        writer = csv.DictWriter(file, my_database[0].keys())
                        writer.writeheader()
                        writer.writerows(lines)
                else:
                    continue
        else:
            print('В файле пока нет никаких данных!')

# lines = list()
# memberName = input("Please enter a member's name to be deleted.")
# with open('mycsv.csv', 'r') as readFile:
#     reader = csv.reader(readFile)
#     for row in reader:
#         lines.append(row)
#         for field in row:
#             if field == memberName:
#                 lines.remove(row)

# with open('mycsv.csv', 'w') as writeFile:
#     writer = csv.writer(writeFile)
#     writer.writerows(lines)