import sys
import os
from PIL import Image

Pictures_folder = sys.argv[1]
New_folder = sys.argv[2]

if not os.path.exists(New_folder):
    os.makedirs(New_folder)

for imageName in os.listdir(Pictures_folder):
    img = Image.open(f'{Pictures_folder}{imageName}')
    name = os.path.splitext(imageName)[0]
    img.save(f'{New_folder}{name}.png', 'png')
    print('Image Converted')
