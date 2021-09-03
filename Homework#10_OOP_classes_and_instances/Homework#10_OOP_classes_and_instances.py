#Ashat_Polvanov

# 1. Создайте класс Vehicle с атрибутами экземпляра max_speed и mileage

class Vehicle:
    max_speed = 200
    mileage = 155000

# 2. Создайте класс Vehicle без переменных и методов

class Vehicle:
    def __init__(self):
        pass

# 3. Создайте класс Person с атрибутами экземпляра first_name,last_name,middle_name,email,
# is_active и методами get_full_name - возвращает полное имя, get_gmail - возвращает только почту с доменом @gmail.com.
# Создайте 5 экземпляров класса Person с разными параметрами и выведите в консоль все параметры созданных вами классов.

class Person:
    first_name = 'Ashat'
    last_name = 'Polvanov'
    middle_name = 'Rustamovich'
    email = 'polvanov_ashat@gmail.com'
    is_active = 'works in SES'

    def __init__(self, first_name, last_name, middle_name, email, is_active):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.email = email
        self.is_active = is_active


    def get_full_name(self):
        first_name = self.first_name
        last_name = self.last_name
        middle_name = self.middle_name
        print(first_name, last_name, middle_name)
        return first_name, last_name, middle_name

    def get_gmail(self):
        email = self.email
        if '@gmail.com' in email:
            print (email)
            return email

def view_full_information(person):
    print(person.first_name, '/', person.last_name, '/', person.middle_name, '/', person.email, '/',\
    person.is_active)


person_1 = Person
view_full_information(person_1)

person_2 = Person('Loginova', 'Larisa', 'Anatolievna', 'larisa@mail.com', 'works in school')
view_full_information(person_2)

person_3 = Person('Ribas', 'Roman', 'Vladislavovich', 'ribas@inbox.ru', 'works as a mechanic')
view_full_information(person_3)

person_4 = Person('Tokareva', 'Elena', 'Vladimirovna', 'elenka_milaya@gmail.com', 'is studying at a university')
view_full_information(person_4)

person_5 = Person('Ten', 'Vladislav', 'Arturovich', 'tenchik99@mail.com', 'works as a salesman')
view_full_information(person_5)
