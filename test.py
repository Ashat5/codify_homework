# import sys
# from PIL import Image
# import os
# from PIL import Image
# from PIL import Image, ImageDraw, ImageFont


# BASE_PATH = sys.path[0] + "/"
# FILE_NAME = BASE_PATH + "test.jpg"
# NEW_FILE_PATH = BASE_PATH + 'modified.jpeg'

# # files_array = os.listdir(BASE_PATH) # all files in directory

# img = Image.open(FILE_NAME)
# draw = ImageDraw.Draw(img)
# draw.text((5,10),'MY PYTHON')
# img.save(NEW_FILE_PATH)
# img.close()
# BASE_PATH = sys.path[0]
# FILE_PATH = BASE_PATH + '/test.jpg'
# img = Image.open(FILE_PATH)
# print(img.size, img.format)
# img.close()

# img = Image.open(FILE_PATH)
# img.thumbnail((100, 100))
# img.save(BASE_PATH + '/MY_THUMBNAIL.JPG')
# img.close()

# BASE_PATH = sys.path[0] + "/"
# FILE_NAME = BASE_PATH + "test.jpg"
# THUMBNAIL_PATH_NAME = BASE_PATH + 'cropped_part.jpeg'

# print(sys.argv[1:])

# box = (100, 100, 400, 400)
# """
# The region is defined by a 4-tuple, where coordinates are (left, upper, right, lower). 
# The Python Imaging Library uses a coordinate system with (0, 0) in the upper left corner. 
# Also note that coordinates refer to positions between the pixels, so the region in the above example is exactly 300x300 pixels.
# """
# try:
#     with Image.open(FILE_NAME) as im:
#         region = im.crop(box)
#         region.save(THUMBNAIL_PATH_NAME, "JPEG")
# except OSError:
#     print("cannot create thumbnail for ", FILE_NAME)

#Создать класс машины с минимум 5-ю полями и 3 методами.

# class Car:
#     wheels = 4
#     doors = 5
#     engine = '5.5L'
#     bumper = 2
#     hood = 1

#     def move(self):
#         print('Car is moving!')

#     def breake_down(self):
#         print('Car is breaking')

# car_1 = Car()
# print(car_1.wheels, car_1.doors)
# car_1.breake_down()

# Создать класс Person с полями first_name,last_name,middle_name,age и определить в нём методы
# __eq__ по длине ФИО
# __add__ по полю age
# __mul__ по полю age

# class Person:
#     def __init__(self, first_name, last_name, middle_name, age ):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.middle_name = middle_name
#         self.age = age

#     def __eq__(self, full_name):
#         return len(self.first_name) + len(self.last_name) + len(self.middle_name) == \
#             len(full_name.first_name) + len(full_name.last_name) + len(full_name.middle_name)

# person_1 = Person('Loginova', 'Larisa', 'Anatolievna', 55)
# person_2 = Person('Ribas', 'Roman', 'Vladislavovich', 46)
# print(person_1 == person_2)


# 2. Создать класс BankAccount с полем value и реализовать методы
#  __eq__ __ge__ __gt__ __lt__ __add__ __mul__
# чтобы они работали с типами int, float.
# Пример:
# banc_acc = BancAccount(30)
# banc_acc == 30 # True
# banc_acc >= 10 #  True
# banc_acc > 40 # False
# banc_acc + 50 # 80
# banc_acc * 2 # 60

class BankAccount:
    def __init__(self, value):
        self.value = value

    def __eq__(self, object):
        return self.value == object

    def __ge__(self, object):
        return self.value >= object.value

    def __gt__(self, object):
        return self.value >= object.value

    def __lt__(self, object):
        return self.value > object.value

    def __add__(self, object):
        return self.value + object.value

    def __mul__(self, object):
        return self.value * object.value

banc_acc = BankAccount(30)
object = 30
print(banc_acc == object)