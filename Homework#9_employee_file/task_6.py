# import PIL
# import sys
# import os
# from PIL import Image



# BASE_PATH = sys.path[0]
# FILE_PATH = BASE_PATH + '/test.jpg'
# img = Image.open(FILE_PATH)
# print(img.size, img.format)
# img.close()

# img = Image.open(FILE_PATH)
# img.thumbnail((100, 100))
# img.save(BASE_PATH, '/my_thumbnail.jpg')
# img.close()

import sys
from PIL import Image


BASE_PATH = sys.path[0] + "/"
FILE_NAME = BASE_PATH + "test.jpg"
THUMBNAIL_PATH_NAME = BASE_PATH + 'cropped_part.jpeg'

print(sys.argv[1:])

box = (100, 100, 400, 400)
"""
The region is defined by a 4-tuple, where coordinates are (left, upper, right, lower). 
The Python Imaging Library uses a coordinate system with (0, 0) in the upper left corner. 
Also note that coordinates refer to positions between the pixels, so the region in the above example is exactly 300x300 pixels.
"""
try:
    with Image.open(FILE_NAME) as im:
        region = im.crop(box)
        region.save(THUMBNAIL_PATH_NAME, "JPEG")
except OSError:
    print("cannot create thumbnail for ", FILE_NAME)