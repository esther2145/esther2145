"""
#file handling
import os
print(os.getcwd)
#change the directory
os.chdir('D:\\vs code')
print(os.getcwd)
# list all files in current directory
print(os.listdir('D://'))
#make new directory
os.mkdir('new_dir')
#rename a directory
os.rename('new_dir','new_dir2')
#remove a directory
import shutil
shutil.rmtree('new_dir')

#photes
import os
import shutil
import PIL
from PIL import Image
from PIL.ExifTags import TAGS

def get_photo_date_taken(photo_path):
    try:
        image = Image.open(photo_path)
        exif = image._getexif()
"""        
