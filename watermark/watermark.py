import os
import sys
from PIL import Image, ImageDraw, ImageFont


LOAD_PATH = sys.path[0] + '/source-images/'
BASE_SAVE_PATH = sys.path[0] + '/output-images/'
IMAGE_EXTENSIONS = ('.png', '.jpg', '.jpeg')
processing_files = os.listdir(LOAD_PATH)


os.mkdir(BASE_SAVE_PATH)
for item in processing_files:
    if item.endswith(IMAGE_EXTENSIONS):
        img = Image.open(LOAD_PATH + item)
        image_name, unnecessary_variable = os.path.splitext(item)
        value = len(image_name) * 22.6
        new_width = img.width - value
        new_height = img.height - 53
        font = ImageFont.truetype('verdana.ttf', size=40)
        draw_text = ImageDraw.Draw(img)
        draw_text.text((new_width, new_height),'%s' % image_name, font=font, fill='yellow')
        img.save(BASE_SAVE_PATH + '%s.jpg' % image_name)
        img.close()        


        

        

