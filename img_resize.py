#importing pillow library
from PIL import Image
#importing os and system
import os, sys
#defining path of the folder to be resized
path = "D:\projects\projects\cat_image"
#openind and getting all the content of the file
dirs = os.listdir( path )
for item in dirs:
    if os.path.isfile(path+item):
        #opening image
        im = Image.open(path+item)
        f, e = os.path.splitext(path+item)
        #resizing in 64x64 size
        imResize = im.resize((64,64), Image.ANTIALIAS)
        #saving image 
        imResize.save(f + ' resized.jpg', 'JPEG', quality=90)


