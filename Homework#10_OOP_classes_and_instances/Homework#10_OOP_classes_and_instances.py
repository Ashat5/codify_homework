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


    def get_full_name(self, first_name, last_name, middle_name):
        return first_name, last_name, middle_name

    def get_gmail(self, email):
        self.email = email
        if '@gmail.com' in email:
            return email

    def view_full_information(self):
        print(self.first_name, '/', self.last_name, '/', self.middle_name, '/', self.email, '/',\
            self.is_active)


person_1 = Person
person_1.view_full_information(Person)

person_2 = Person('Loginova', 'Larisa', 'Anatolievna', 'larisa@mail.com', 'works in school')
person_2.view_full_information()

person_3 = Person('Ribas', 'Roman', 'Vladislavovich', 'ribas@inbox.ru', 'works as a mechanic')
person_3.view_full_information()

person_4 = Person('Tokareva', 'Elena', 'Vladimirovna', 'elenka_milaya@gmail.com', 'is studying at a university')
person_4.view_full_information()

person_5 = Person('Ten', 'Vladislav', 'Arturovich', 'tenchik99@mail.com', 'works as a salesman')
person_5.view_full_information()