#Ashat_Polvanov

# 1. Определите класс Book со следующими атрибутами: Название, Автор (полное имя), Цена.
# Определите конструктор, используемый для инициализации атрибутов метода значениями, введенными пользователем.
# Задайте метод View() для отображения информации для текущей книги.
# Напишите программу для тестирования класса Book.

class Book:
    def __init__(self, book_title, autor_name, price_of_book):
        self.book_title = book_title
        self.autor_name = autor_name
        self.price_of_book = price_of_book


    def view_information_about_book(self):
        print('''Название книги: {0}
Автор: {1}
Цена: {2}'''.format(self.book_title, self.autor_name, self.price_of_book))

my_book = Book('Три мушкетера', 'Александр Дюма', 5000)
my_book.view_information_about_book()

# 2. Определите класс Playlist, его метод __init__() должен иметь два аргумента: self,
# song_list - список из классов Song.
# Класс Song с полями:
# - name - название песни,
# - lyric - слова песни.
# Создайте список из классов песней и передайте в класс Songs.
# Внутри класса Playlist создайте метод sing_me_a_song(song_name), который находит песню по её названию и выводит
# каждый элемент текста песни в отдельной строке. Обработайте возможные ошибки.

class Playlist():
    def __init__(self, song_list = []):
        self.song_list = song_list

    def sing_me_a_song (self, song_name):    
        if song_name in self.song_list:
            print(self.song_list[1])

        
class Song:
    def __init__(self, name, lyric):
        self.name = name
        self.lyric = lyric


song = Song('Научусь летать', '''  Он носит крылья в рюкзаке,
                                    Мечтает и грустит о ком-то,
                                    А на картинке так жесток.
                                    Живет в пальто коротком чьем-то.
                                    Он ищет ту, что не прощает,
                                    Не придает, не отпускает.
                                    Такой я есть, такой не знаю,
                                    Но только, только обещаю...''')
my_playlist = Playlist([song])

Playlist.sing_me_a_song(my_playlist, song_name = input('Введите название песни: '))

# 3. Игра в кости для 2ух игроков, игроки по очереди бросают кости, начинает первый игрок, пока он вводит в консоль слово:
#  mix - кости перемешиваются(максимум 5 раз, иначе автопоражения, предупреждать об оставшемся количестве перемешиваний),
#  если вводит
# любое другое слово кости бросаются и показывается результат(он записывается), потом очередь 2ого игрока.
# После этого тоже самое делает 2ой игрок и так 3 раза, у кого по итогу этих 3-ёх раз будет большее число - тот победил.

import random



def dice_rolling(max_overexpression):
    overexpression = 0
    while overexpression <= 5:
        player_input = input('''Введите "mix" чтобы перемешать кости или любую другую клавишу чтобы бросить кости
(максимальное количество перемешиваний "5": ''') 
        if player_input == 'mix':
            overexpression += 1
            print('Перемешивание костей(оставшееся количество перемешиваний : {}'.format(max_overexpression - overexpression))
        else:
            number_on_the_dice = random.randint(1, 6)
            second_number_on_the_dice = random.randint(1, 6) 
            print('Ваши числа: {0} {1}'.format(number_on_the_dice, second_number_on_the_dice))
            return number_on_the_dice + second_number_on_the_dice
    if overexpression > 5:
        print('Превышено максимальное количество перемешиваний! ВЫ ПРОИГРАЛИ!')
        return None

def scoring(results, first_player_throw, first_player_result, second_player_result):
    if first_player_throw == 7:
        if first_player_result > second_player_result:
            print('ПЕРВЫЙ ИГРОК ПОБЕДИЛ!')
            return
        else:
            print('ВТОРОЙ ИГРОК ПОБЕДИЛ!')
            return

    if first_player_throw in (1, 3, 5):
        first_player_result += results
        return first_player_result
        
    else:
        second_player_result += results
        return second_player_result
        


def main():
    print('*' * 120)
    print('''                          *****ДОБРО ПОЖАЛОВАТЬ В ИГРУ КОСТИ*****''')
    print('*' * 120)
    max_overexpression = 5
    first_player_throw = 1
    first_player_result = 0
    second_player_result = 0
    number_of_shot = 1
    while number_of_shot <= 6:
        if number_of_shot in (1, 3, 5):
            print('Первый игрок бросает!')
            number_of_shot += 1
            result_1_player = dice_rolling(max_overexpression)

            if result_1_player == None:
                break
            first_player_result = scoring(result_1_player, first_player_throw, first_player_result, second_player_result)
            first_player_throw += 1
        else:
            print('Второй игрок бросает!')
            number_of_shot += 1
            result_2_player = dice_rolling(max_overexpression)

            if result_2_player == None:
                break
            second_player_result = scoring(result_2_player, first_player_throw, first_player_result, second_player_result)
            first_player_throw += 1

    end_of_game = scoring(result_2_player, first_player_throw, first_player_result, second_player_result)
    if end_of_game == None:
        print('Спасибо за игру!')

main()


# 4. Функции для расчета стоимости вашей поездки:
# Определите функцию hotel_cost с одним аргументом nights в качестве входных данных. Стоимость проживания в отеле составляет 
# 140 долларов за ночь. Таким образом, функция hotel_cost должна возвращать 140 * nights.
# Определите функцию plane_ride_cost, которая принимает на вход строку city. Функция должна возвращать разные цены в зависимости
#  от местоположения, как в примере кода выше. Ниже приведены допустимые пункты назначения и соответствующие им цены туда и обратно.
# "Шарлотт": 183
# "Тампа": 220
# "Питтсбург": 222
# "Лос-Анджелес": 475
# -Под существующим кодом определите функцию rental_car_cost с аргументом days. Рассчитайте стоимость аренды автомобиля:
#  Каждый день аренды автомобиля стоит $40.(cost=40*days) Если вы арендуете автомобиль на 7 или более дней, вы получаете
#  скидку $50(cost-=50). В качестве альтернативы (elif), если вы арендуете автомобиль на 3 или более дней, вы получите скидку $20.
#  Вы не можете получить обе вышеуказанные скидки. Верните эту стоимость. -Затем определите функцию trip_cost, которая
#  принимает два аргумента, город и дни. Как и в примере выше, пусть ваша функция возвращает сумму вызовов функций
#  rental_car_cost(days), hotel_cost(days) и plane_ride_cost(city).
# Измените определение функции trip_cost. Добавьте третий аргумент, spending_money.
#  Измените то, что делает функция trip_cost. Добавьте переменную `spending_money к возвращаемой ею сумме.

def get_hotel_cost(nights):
    return 140 * nights

def get_plane_ride_cost(citys, city):
    for i in citys:
        for item in i:
            if city == item:
                return i[item]

def get_rental_car_cost(days):
    cost = 40 * days
    if days >= 7:
        cost -= 50
    elif days < 7 and days >= 3:
        cost -= 20
    return cost

def get_trip_cost(nights, citys, city, days, spending_money):
    return get_hotel_cost(nights) + get_plane_ride_cost(citys, city) + get_rental_car_cost(days) + spending_money

def main():
    citys = [{"Шарлотт": 183},
             {"Тампа": 220},
             {"Питтсбург": 222},
             {"Лос-Анджелес": 475}]
    for i in citys:
        for item in i:
            print(item)
    city = input('Введите город в который хотите полететь: ')
    
    nights = None
    days = None
    spending_money = None
    while type(nights) != int:
        try:
            nights = int(input('Введите количество ночей которые хотите провести в отеле: '))
        except ValueError:
            print('Вы должны ввести цифру!')  
    

    while type(days) != int:
        try:
            days = int(input('Введите на сколько дней хотите орендовать авто: '))
        except ValueError:
            print('Вы должны ввести цифру!') 
    

    while type(spending_money) != int:
        try:
            spending_money = int(input('Введите количество средств на дополнительные расходы: '))
        except ValueError:
            print('Вы должны ввести цифру!')
    trip_cost = get_trip_cost(nights, citys, city, days, spending_money)
    print('На поездку в {0} вам понадобится {1} $'.format(city, trip_cost))

main()