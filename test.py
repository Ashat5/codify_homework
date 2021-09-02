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

class Car:
    wheels = 4
    doors = 5
    engine = '5.5L'
    bumper = 2
    hood = 1

    def move(self):
        print('Car is moving!')

    def breake_down(self):
        print('Car is breaking')

car_1 = Car()
print(car_1.wheels, car_1.doors)
car_1.breake_down()