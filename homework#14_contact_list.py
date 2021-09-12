#Ashat_Polvanov

# Создайте класс Contact, и объявите в конструкторе(__init__) ему поля
# name, last_name и number. Далее, создайте класс ContactList, в нем
# объявите переменную contacts_list = [], после, реализуйте три метода,
# add_contact(), который берет в аргументы объект класса Contact и
# добавляет в лист contacts_list, seacrh_contact(), который должен вернуть
# нам контакт если такой имеется в списке, remove_contact() который
# должен удалить найденный контакт, эти методы также принимают в
# качества аргумента объект класса Contact. Создайте несколько объектов
# класса Contact, и объект класса ContactList, воспользуйтесь всеми его
# методами.


class Contact():
    def __init__(self, name, last_name, number):
        self.name = name
        self.last_name = last_name
        self.number = number

class ContactList():
    contact_list = []

    def add_contact(self, user):
        users_list = [user.name, user.last_name, user.number]
        self.contact_list.append(users_list)

    def search_contact(self, user):
        for i in self.contact_list:
            if user.name and user.last_name and user.number in i:
                print(i)
                return i

    def remove_contact(self, user):
        for i in self.contact_list:
            if user.name and user.last_name and user.number in i:
                self.contact_list.remove(i)
      

user_1 = Contact('Larisa', 'Loginova', 1)
user_2 = Contact('Elena', 'Tokareva', 2)
user_3 = Contact('Roman', 'Ribas', 3)
my_contact_list = ContactList()
my_contact_list.add_contact(user_1)
my_contact_list.add_contact(user_2)
my_contact_list.add_contact(user_3)
print(my_contact_list.contact_list)
my_contact_list.search_contact(user_2)
print(my_contact_list.contact_list)
my_contact_list.remove_contact(user_2)
print(my_contact_list.contact_list)