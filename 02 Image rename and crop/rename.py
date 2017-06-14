import os
from PIL import Image

def rename():
    Dir_Path = ''
    count = 1
    for file in os.listdir(Dir_Path+'images\\'):
        print('images\\'+file)
        image = Image.open('images\\'+file)
        image = image.crop((1,91,1280,625))
        image.save(Dir_Path+'ans_image\\'+str(count)+'.jpg')
        count+=1

if __name__ == '__main__':
    rename()
