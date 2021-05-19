from PIL import Image
import os

folder_with_maps = 'maps'
path_of_maps = []


def get_images_from_dir(folder='maps'):
    path_ = []
    for root, dirs, files in os.walk(folder):
        for filename in files:
            if filename.lower().endswith(('.jpg', '.gif', '.png', '.jpeg', '.tif', '.bmp')):
                print(root+'\\'+filename)
                path_.append(root+'\\'+filename)
    return path_


replace_dict = {'~': '-',
                '!': '1'}
spec_symbols = {'°', '`', '‘', '*', '^', '#', '@', '.', '"', "'", '%', ':', ';', ',', '$', '№'}

# for i in replace_dict:
#     print(i)
#     print(replace_dict.get(i))

# with open('./config.ini', 'r') as inp:
#     file = {}
#     for line in inp:
#         word = []
#         word = line.split('=')
#         word[1] = word[1].replace('\n', '')
#         file.update([(word[0], word[1])])

file = {'tesseract_path': 'C:/Program Files/Tesseract-OCR/tesseract.exe', 'folder_with_maps': 'None', 'target_folder': 'None', 'lang': 'rus+eng', 'height_of_head': '8'}
with open('./config.ini', 'w') as inp:
    for i in file:
        print(i)
        inp.write(i + '=' + file.get(i) + '\n')

# print(file)
