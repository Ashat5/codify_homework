#Ashat_Polvanov

# 1. Напишите программу для создания 26 текстовых файлов с именами A.txt, B.txt и так далее до Z.txt, в каждом файле будет его имя, 
# пример:
# Файл a.txt - содержит a
# Файл b.txt - содержит b 
# 2. Добавьте возможность удаления этих 26 файлов.
import os
import sys


alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in alphabet:
  with open(os.path.join(sys.path[0], '%s.txt' % i), 'w') as file:
    file.write('%s' % i)
    file.close()


users_input = input('''
                      Вы хотите удалить созданные текстовые файлы?
                      Для удаления введите "да";
                      Для выхода из приложения нажмите любую клавишу;
                      Ваш ввод: ''')
users_input = users_input.lower()
if users_input == 'да':
  for i in alphabet:
    os.remove(os.path.join(sys.path[0], '%s.txt' % i))
    
