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

for i in replace_dict:
    print(i)
    print(replace_dict.get(i))
