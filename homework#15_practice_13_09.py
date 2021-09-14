#Ashat_Polvanov

# 3.Создайте класс Plane, конструктор которого принимает brand,
# model. Пропишите в классе метод __str__. Пусть он возвращает
# brand и model самолета. Создайте подклассы Destroyer
# (Истребитель), Stelth (Стэлс), Kukuruznik (Кукурузник). В классе
# Destroyer перегрузите метод конструктор с помощью функции
# super(), добавьте поле can_fire = True. Также создайте в классе
# Destroyer метод fire (стрелять). В классе Stelth перегрузите метод
# конструктор с помощью функции super(), добавьте поле is_visible
# = False. Также добавьте метод hide (прятаться) в класс Stelth. А в
# классе Kukuruznik перегрузите метод конструктор с помощью
# функции super(), добавьте поле can_fertilize = True. Создайте в
# классе метод fertilize (распылять удобрения).Также создайте
# класс миксин SwimMixin, который будет иметь метод swim().
# Унаследуйтесь от этого класса миксина для классов Destroyer,
# Stelth, Kukuruznik. Используйте созданные классы и методы.


class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self): 
        print(self.brand , self.model)      # для проверки
        return self.brand , self.model
        

class SwimMixin:
    def __init__(self):
      pass

    def swim(self):
      print('I can swim!')

class Destroyer(Plane, SwimMixin):
    def __init__(self, brand, model, can_fire = True):
        self.can_fire = can_fire
        super().__init__(brand, model)

    def fire(self):
        print('I can shoot!')

class Stelth(Plane, SwimMixin):
    def __init__(self, brand, model, is_visible = False):
        self.is_visible = is_visible
        super().__init__(brand, model) 

    def hide(self):
        print("I'm invisible")

      

class Kukuruznik(Plane, SwimMixin):
    def __init__(self, brand, model, can_fertilize = True):
        self.can_fertilize = can_fertilize
        super().__init__(brand, model)  

    def fertilize(self):
        print('I can fertilize')

my_plane = Plane('BMW', 'X10')
my_plane.__str__()
my_destroyer = Destroyer('test', 'test')
my_destroyer.__str__()
my_destroyer.fire()
my_destroyer.swim()
my_stelth = Stelth('test_1', 'test_1')
my_stelth.__str__()
my_stelth.hide()
my_stelth.swim()
my_kukuruznik = Kukuruznik('test_2', 'test_2')
my_kukuruznik.__str__()
my_kukuruznik.fertilize()
my_kukuruznik.swim()

# 4.Напишите функцию go_for_a_walk(), которая зовет погулять. Она будет
# распечатывать на экран "Давай, пойдем погуляем на улице!" Напишите
# декоратор, который будет принимать параметр temperature (декоратор тройной
# вложенности). Температуру должен вводить пользователь. Добавьте проверку
# на тип получаемых данных от пользователя используя конструкцию try - except.
# Переведите данные в int и прокиньте в декоратор.
# Если температура больше 10 С, то декоратор должен вызвать функцию
# go_for_a_walk и затем распечатать "На улице тепло, давай погуляем, я не
# против!". Если от 0 до 10 С, то он вызовет функцию и распечатает "Прохладно.
# Надо одеться!", если от -10 до 0 (не включая 0), то - "Холодно. Потеплее
# оденься и пойдем!", если меньше -10, то "Мороз. Лучше давай дома посидим,
# фильм посмотрим!"

def decorator(func):
    def weather_treatment(temperature):
        if temperature > 10:
            func(temperature)
            print("На улице тепло, давай погуляем, я не против!")
        elif temperature in range (0, 11):
            func(temperature)
            print("Прохладно. Надо одеться!")
        elif temperature in range (-10, 0):
            func(temperature)
            print("Холодно. Потеплее оденься и пойдем!")
        elif temperature < -10:
            func(temperature)
            print("Лучше давай дома посидим, фильм посмотрим!")
    return weather_treatment

@decorator
def go_for_a_walk(temperature):
    print("Давай, пойдем погуляем на улице!")

def main():
    user_input_temperature = False
    while user_input_temperature == False:
        try:
            user_input_temperature = int(input('Введите какая сейчас температура на улице: '))
            if user_input_temperature not in range (-50, 50):
                raise Exception ('Введите корректную температуру!')
        except ValueError:
            print('Температура вводится цифрами!')
        except Exception as e:
            print (e)
            user_input_temperature = False
    if user_input_temperature in range (-50, 50):
        go_for_a_walk(user_input_temperature)
    else:
        user_input_temperature = False
    

main()