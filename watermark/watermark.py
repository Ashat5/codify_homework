import os
import sys
from PIL import Image, ImageDraw, ImageFont


LOAD_PATH = sys.path[0] + '/source-images/'
BASE_SAVE_PATH = sys.path[0] + '/output-images/'
IMAGE_EXTENSIONS = ('.png', '.jpg', '.jpeg')
processing_files = os.listdir(LOAD_PATH)


os.mkdir(BASE_SAVE_PATH)
for k in processing_files:
    if k.endswith(IMAGE_EXTENSIONS):
        img = Image.open(LOAD_PATH + k)
        kn, kext = os.path.splitext(k)
        insertion_coordinates = []
        value = len(kn) * 22.6
        new_width = img.width - value
        new_height = img.height - 53
        insertion_coordinates.append(new_width)
        insertion_coordinates.append(new_height)
        insertion_coordinates = tuple(insertion_coordinates)
        font = ImageFont.truetype('verdana.ttf', size=40)
        draw_text = ImageDraw.Draw(img)
        draw_text.text(insertion_coordinates,'%s' % kn, font=font, fill='yellow')
        img.save(BASE_SAVE_PATH + '%s.jpg' % kn)
        img.close()        


        

        

