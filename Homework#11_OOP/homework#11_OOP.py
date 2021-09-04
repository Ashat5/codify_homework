#Ashat_Polvanov

# Нужно создать класс User(пользователь), у которого есть такие свойства: username, email, password
# Создать еще один класс Group, у которого есть свойство users - это будет список, по умолчанию пустой
# Затем создать класс TablePrinter, у которого будет метод(функция) print(), в который можно будет передать объект класса Group,
# а TablePrinter распечатает на экран список всех пользователей в этой группе. Таблица должна быть такой:
 
# TEXT
# username | email | password
# master_alish | masteraalish@gmail.com | ******
# monreal | monrealdesign@vk.ru | ********
# santa_barbara | disco@mail.com | ******
 
# Сверху обязательно идет заголовок таблицы. Пароли заменяем на звездочки, так как пароли не принято показывать
# нигде для безопасности.
# Также у класса TablePrinter должен быть второй метод print_only_gmail() который также принимает объект класса Group,
# и также выводит список пользователей. Но только тех пользователей у которых почта @gmail.com.

class User:
    def __init__(self, username, email, password):
        self.username = username 
        self.email = email
        self.password = password

class Group:
    def __init__(self, users = []):
        self.users = users


class TablePrinter:
    def print_all_users(group): 
        print('username | email | password') 
        for item in group.users:
                print(item.username +' | ' + item.email +' | ' + '*****')

    def print_only_gmail(group):
        print('username | email | password')
        for item in group.users:
            if '@gmail.com' in item.email:
                print(item.username  +' | ' + item.email  +' | ' + '*****')

user1 = User('Test', 'test@gmail.com', 12345)
user2 = User('Test2', 'test2@inbox.ru', 12345678)
user3 = User('Test3', 'test3@gmail.com', 12344566778)

group = Group([user1, user2, user3])
TablePrinter.print_all_users(group)
TablePrinter.print_only_gmail(group)


    
