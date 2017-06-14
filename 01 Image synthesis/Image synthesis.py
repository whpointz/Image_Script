# -*- coding:utf-8 -*-
from PIL import Image
import random
image_size = 512
row_num = 6 #行
col_num = 5 #列
line = 80


arr = [ ['00.bmp', '01.bmp', '02.bmp', '03.bmp', '04.bmp'],
        ['10.bmp', '11.bmp', '12.bmp', '13.bmp', '14.bmp'],
        ['20.bmp', '21.bmp', '22.bmp', '23.bmp', '24.bmp'],
        ['30.bmp', '31.bmp', '32.bmp', '33.bmp', '34.bmp'],
        ['40.bmp', '41.bmp', '42.bmp', '43.bmp', '44.bmp'],
        ['50.bmp', '51.bmp', '52.bmp', '53.bmp', '54.bmp'],
       ]


toImage = Image.new('RGBA',(image_size*col_num + line*(col_num+1),image_size*row_num+line*(row_num+1)))
for i in range(row_num):#6
    for j in range(col_num):#5

        fromImge = Image.open(arr[i][j])
        loc = (j * image_size + line*(j+1), i * image_size+ line*(i+1))
        print(loc)
        toImage.paste(fromImge, loc)

#draw row line ---
for i in range(row_num+1):#7
    for j in range(image_size*col_num + line*(col_num+1)):
        toImage.putpixel([j, i * image_size + i * line  + line / 2 - 2], (100, 100, 100))
        toImage.putpixel([j, i * image_size + i * line  + line / 2 -1], (100, 100, 100))
        toImage.putpixel([j, i * image_size + i * line  + line / 2 ],(100,100,100))
        toImage.putpixel([j, i * image_size + i * line  + line / 2 +1],(100,100,100))
        toImage.putpixel([j, i * image_size + i * line  + line / 2 + 2], (100, 100, 100))

#draw col line |
for i in range(col_num+1):#6
    for j in range(image_size*row_num + line*(row_num+1)):
        toImage.putpixel([ i * image_size + i * line  + line / 2 - 2,j], (100, 100, 100))
        toImage.putpixel([ i * image_size + i * line  + line / 2 -1,j], (100, 100, 100))
        toImage.putpixel([ i * image_size + i * line  + line / 2 ,j],(100,100,100))
        toImage.putpixel([ i * image_size + i * line  + line / 2 +1,j],(100,100,100))
        toImage.putpixel([ i * image_size + i * line  + line / 2 + 2,j], (100, 100, 100))


toImage = toImage.crop((line/2-2,line/2-2,image_size*col_num + line*col_num + line/2 + 2,image_size*row_num+line*row_num+line/2 + 2))

toImage.save('answer.png')