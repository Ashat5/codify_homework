import os
import sys
from PIL import Image, ImageDraw, ImageFont


LOAD_PATH = sys.path[0] + '/source-images/'
BASE_SAVE_PATH = sys.path[0] + '/output-images/'
IMAGE_EXTENSIONS = ('.png', '.jpg', '.jpeg')
processing_files = os.listdir(LOAD_PATH)

try:
    path_to_save = sys.argv[1]
except IndexError:
    path_to_save = BASE_SAVE_PATH

os.mkdir(path_to_save)
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
        img.save(path_to_save + '%s.jpg' % kn)
        img.close()        


        

        


        # watermark = kn
        # new_img = Image.new('RGB', size = (size)) #BASE_SAVE_PATH + '%s.jpg' % kn
        # position = (img.width - watermark.width,
        #             img.height - watermark.height)
        # img.paste(watermark, position, watermark)







# img = Image.open(LOAD_PATH)
# draw = ImageDraw.Draw(img)
# draw.text((5,10),'MY PYTHON')
# img.save(BASE_SAVE_PATH)
# img.close

# im = Image.open('d:/beach.jpeg')
# watermark = Image.open('d:/logo.png')
# # Вычисляем расположение watermark
# position = (im.width - watermark.width,
#              im.height - watermark.height)
# im.paste(watermark, position, watermark)

# im.show()