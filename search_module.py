import pytesseract as tsrct
from PIL import Image
import os
import shutil
import datetime
from pathlib import Path

# Настройки
# Путь к установленному tesseract
# tsrct.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# height_of_head = 8  # Высота шапки в % (примерно 8)
config = r'--oem 3 --psm 6'  # Конфигурация tesseract
# folder_with_maps = 'maps'

replace_dict = {'~': '-',
                '!': '1',
                '—': '-'}
spec_symbols = ['°', '`', '‘', '*', '^', '#', '@', '.', '"', "'",
                '%', ':', ';', '$', '№', '~', '=', '+', '(', ')',
                '{', '}']
nomenclature = None


def save_logging(conf=None, str=None):
    """
    Сохранение логов в файле
    :param conf: Словарь с настройками
    :param str: Строка, которую необходимо сохранить в лог
    :return: None
    """
    if conf is None:
        conf = {}
    with open('logs.log', 'a') as f:
        if str is None:
            # При запуске модуля создаем шапку с временем запуска и текущими настройками
            f.write(f'*'*50 + '\n')
            now = datetime.datetime.now()
            f.write(f'{now.strftime("%d-%m-%Y %H:%M:%S")}\n')
            if conf != {}:
                f.write(f"tesseract_path={conf['tesseract_path']}\n")
                f.write(f"folder_with_maps={conf['folder_with_maps']}\n")
                f.write(f"target_folder={conf['target_folder']}\n")
                f.write(f"lang={conf['lang']}\n")
                f.write(f"height_of_head={conf['height_of_head']}\n\n")
        else:
            f.write(f'{str}\n')
    return


def get_images_from_dir(folder='maps'):
    """
    Поиск всех изображений в папке
    :param folder: Путь папки
    :return: Массив с путями всех найденных изображений
    """
    path_ = []
    for root, dirs, files in os.walk(folder):
        for filename in files:
            if filename.lower().endswith(('.jpg', '.gif', '.png', '.jpeg', '.tif', '.bmp')):
                # print(root+'\\'+filename)
                path_.append(root+'\\'+filename)
    return path_


def get_nomenclature(data_string):
    """
    Поиск номенклатуры карты
    :param data_string: Считанный с изображения текст
    :return: Строка с номенклатурой или None, если номенклатура не определена.
    """
    # Пытаемся найти слова, схожие с номенклатурой
    data = data_string.split()
    try:
        save_logging(str=f'Data from image {data}')
    except Exception:
        pass
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

    # Если слов напоминающих номенклатуру не удалось обнаружить, возвращаем None
    save_logging(str=f'Potential nomenclatures: {potential_nomenclature}')
    if len(potential_nomenclature) == 0:
        # print(f'Номенклатура не найдена!')
        return None
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


def init(conf=None):
    """
    Инициализация модуля
    :param conf: значения конфигурационного файла
    :return: None
    """
    if conf is None:
        conf = {}
    save_logging(conf=conf)

    tsrct.pytesseract.tesseract_cmd = conf['tesseract_path']
    path_of_maps = get_images_from_dir(conf['folder_with_maps'])
    target_folder = conf['target_folder']
    height_of_head = int(conf['height_of_head'])
    lang = conf['lang']
    for path in path_of_maps:
        # Подключение фото
        try:
            img = Image.open(path)
        except Exception:
            continue
        # Вычислим размер фото и шапки
        width, height = img.size
        height_head = int(height * height_of_head / 100)
        # Вырезаем шапку, в которой находится номенклатура
        img = img.crop((0, 0, width, height_head))
        # img.show()
    
        # Определяем текст на изображении
        # Лучше использовать rus+eng
        data_string = tsrct.image_to_string(img, lang=lang, config=config)
        # Листинг
        save_logging(str=f'{path_of_maps.index(path) + 1} / {len(path_of_maps)} | '
                         f'{((path_of_maps.index(path) + 1) / (len(path_of_maps)) * 100)}%')
        save_logging(str=f'{path}')
        print(f'*'*50)
        print(f'{path_of_maps.index(path) + 1} / {len(path_of_maps)} | '
              f'{((path_of_maps.index(path) + 1) / (len(path_of_maps)) * 100)}%')
        print(f'{path}')
        nomenclature = None
        try:
            nomenclature = get_nomenclature(data_string)
        except Exception:
            pass
        print(nomenclature)
        save_logging(str=f'Nomenclature {nomenclature}')

        rashirenie = Path(path).suffix
        file_name = ''
        if nomenclature is None:
            # file_name = f'{path_of_maps.index(path) + 1}-{len(path_of_maps)}'
            save_logging(str=f'Skipped\n')
            continue
        else:
            file_name = f'{nomenclature}'
        i = 0
        while os.path.exists(target_folder+f'/{file_name}{rashirenie}'):
            i += 1
            if not os.path.exists(target_folder + f'/{file_name}({i}){rashirenie}'):
                file_name += f'({i})'

        shutil.copy(path, target_folder+f'/{file_name}{rashirenie}')
        save_logging(str=f'Saved as {target_folder}/{file_name}{rashirenie}\n')

    return