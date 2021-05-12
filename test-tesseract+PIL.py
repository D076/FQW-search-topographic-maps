import pytesseract as tsrct
from PIL import Image
import os


def get_images_from_dir(folder='maps'):
    path_ = []
    for root, dirs, files in os.walk(folder):
        for filename in files:
            if filename.lower().endswith(('.jpg', '.gif', '.png', '.jpeg', '.tif', '.bmp')):
                # print(root+'\\'+filename)
                path_.append(root+'\\'+filename)
    return path_


def get_nomenclature(data_string):
    # Пытаемся найти слова, схожие с номенклатурой
    data = data_string.split()
    potential_nomenclature = []
    prev_word = data[0]
    for word in data:
        if '-' not in word or len(word) < 2:
            prev_word = word
            continue
        # print(word)
        if word[0] == '-':
            new_word = prev_word + word
            potential_nomenclature.append(new_word)
        else:
            potential_nomenclature.append(word)
        prev_word = potential_nomenclature[-1]
        # print(word)

    # Если слов напоминающих номенклатуру не удалось обнаружить, возвращаем None
    if len(potential_nomenclature) == 0:
        return None
        # print(f'Номенклатура не найдена!')
    else:
        # Корректируем слова
        for word in potential_nomenclature:
            for i in replace_dict:
                j = replace_dict.get(i)
                word = word.replace(i, j)

        # Удаляем некорректные слова
        for word in potential_nomenclature:
            for i in spec_symbols:
                if i in word:
                    potential_nomenclature.remove(word)
                    break
        if len(potential_nomenclature) != 0:
            return potential_nomenclature[-1]
        else:
            return None


# Настройки
# Путь к установленному tesseract
tsrct.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
height_of_head = 8  # Высота шапки в % (примерно 8)
config = r'--oem 3 --psm 6'  # Конфигурация
folder_with_maps = 'maps'

replace_dict = {'~': '-',
                '!': '1'}
spec_symbols = ['°', '`', '‘', '*', '^', '#', '@', '.', '"', "'",
                '%', ':', ';', '$', '№', '~', '=', '+', '(', ')',
                '{', '}']
nomenclature = None
path_of_maps = get_images_from_dir(folder_with_maps)

for path in path_of_maps:
    # Подключение фото
    # img = Image.open(path_of_maps[0])
    img = Image.open(path)
    # Вычислим размер фото и шапки
    width, height = img.size
    height_head = int(height * height_of_head / 100)
    # Вырезаем шапку, в которой находится номенклатура
    img = img.crop((0, 0, width, height_head))
    # img.show()

    # Определяем текст на изображении
    # Лучше использовать rus+eng
    data_string = tsrct.image_to_string(img, lang='rus+eng', config=config)
    # Листинг
    # print(data_string)
    print(f'*'*50)
    print(f'{path_of_maps.index(path) + 1} / {len(path_of_maps)} | '
          f'{((path_of_maps.index(path) + 1) / (len(path_of_maps)) * 100)}%')
    print(f'{path}')
    nomenclature = get_nomenclature(data_string)
    print(nomenclature)


# # Подключение фото
# img = Image.open(path_of_maps[3])
# # Вычислим размер фото и шапки
# width, height = img.size
# height_head = int(height * height_of_head / 100)
# # Вырезаем шапку, в которой находится номенклатура
# img = img.crop((0, 0, width, height_head))
# # img.show()
#
# # Определяем текст на изображении
# # Лучше использовать rus+eng
# data_string = tsrct.image_to_string(img, lang='rus+eng', config=config)
# print(data_string)
# print(f'*'*50)
# nomenclature = get_nomenclature(img, data_string)
# # print(f'{path}')
# print(nomenclature)