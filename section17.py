import sys
import os
from PIL import Image

# img = Image.open('pikachu.jpg')
# print(img.mode)
# filtered_img = img.convert('L')
# filtered_img = img.filter(ImageFilter.BLUR)
# # filtered_img.save("blur.png", 'png')
# filtered_img.show()
# crooked = filtered_img.rotate(180)
# resize = filtered_img.resize((300, 300))
# crop = filtered_img.crop(100, 100, 400, 400)

# # new_img = img.resize


# path = './new'
# pathExist = os.path.exists(path)
# print(pathExist)

Pictures_folder = sys.argv[1]
New_folder = sys.argv[2]

if not os.path.exists(New_folder):
    os.makedirs(New_folder)

for imageName in os.listdir(Pictures_folder):
    img = Image.open(f'{Pictures_folder}{imageName}')
    name = os.path.splitext(imageName)[0]
    img.save(f'{New_folder}{name}.png', 'png')
    print('Image Converted')
