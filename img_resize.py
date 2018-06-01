#!/usr/bin/python
from PIL import Image
import os, sys

path = "D:\projects\projects\cat_image"
dirs = os.listdir( path )
for item in dirs:
    if os.path.isfile(path+item):
        im = Image.open(path+item)
        f, e = os.path.splitext(path+item)
        imResize = im.resize((64,64), Image.ANTIALIAS)
        imResize.save(f + ' resized.jpg', 'JPEG', quality=90)


