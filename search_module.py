import pytesseract as tsrct
from PIL import Image
import os
import shutil
import datetime
from functools import partial
import time, threading
from pathlib import Path
import tkinter as tk
from tkinter import ttk
import queue


# Настройки
config = r'--oem 3 --psm 6'  # Конфигурация tesseract
DEBUG = False


replace_dict = {'~': '-',
                '!': '1',
                'l': '1',
                '—': '-',
                'У': 'V',
                'Ш': 'III'}
spec_symbols = ['°', '`', '‘', '*', '^', '#', '@', '.', '"', "'",
                '%', ':', ';', '$', '№', '~', '=', '+', '(', ')',
                '{', '}', '[', ']']
first_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                'H', 'I', 'G', 'K', 'L', 'M', 'N',
                'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'Z'
                'А', 'М', 'О', 'Т', 'Е', 'К', 'Н',
                '0', '1', '2', '3', '4', '5', '6',
                '7', '8', '9', '10', '11', '12', '13',
                '14', '15', '16', '17', '18', '19', '20', '21']
second_letter = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
                '31', '32', '33', '34', '35', '36', '37', '38', '39', '40',
                '41', '42', '43', '44', '45', '46', '47', '48', '49', '50',
                '51', '52', '53', '54', '55', '56', '57', '58', '59', '60']
third_letter = ['А', 'Б', 'В', 'Г', '1', '2', '3', '4', 'A',
                '01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
                '31', '32', '33', '34', '35', '36',
                'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI',
                'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX',
                'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI', 'XXVII', 'XXVIII',
                'XXIX', 'XXX', 'XXXI', 'XXXII', 'XXXIII', 'XXXIV', 'XXXV', 'XXXVI',
                '001', '002', '003', '004', '005', '006', '007', '008', '009', '010', '011', '012', '013', '014',
                '015', '016', '017', '018', '019', '020', '021', '022', '023', '024', '025', '026', '027', '028',
                '029', '030', '031', '032', '033', '034', '035', '036', '037', '038', '039', '040', '041', '042',
                '043', '044', '045', '046', '047', '048', '049', '050', '051', '052', '053', '054', '055', '056',
                '057', '058', '059', '060', '061', '062', '063', '064', '065', '066', '067', '068', '069', '070',
                '071', '072', '073', '074', '075', '076', '077', '078', '079', '080', '081', '082', '083', '084',
                '085', '086', '087', '088', '089', '090', '091', '092', '093', '094', '095', '096', '097', '098',
                '099', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112',
                '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126',
                '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140',
                '141', '142', '143', '144',
                '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26',
                '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43',
                '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60',
                '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77',
                '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94',
                '95', '96', '97', '98', '99']
fourth_letter = ['A', 'Б', 'В', 'Г', 'A']
fifth_letter = ['а', 'б', 'в', 'г', 'a']
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
    if DEBUG:
        print(data_string)
    data = data_string.split()
    if DEBUG:
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
        # print(potential_nomenclature)
        new_potential_nomenclature = []
        for word in potential_nomenclature:
            for i in replace_dict:
                j = replace_dict.get(i)
                word = word.replace(i, j)
            new_potential_nomenclature.append(word)
        potential_nomenclature = list(new_potential_nomenclature)
        print(potential_nomenclature)
        # Удаляем некорректные слова
        copy_potential_nomenclature = list(potential_nomenclature)
        for word in potential_nomenclature:
            try:
                if word.split('-')[0] not in first_letter:
                    print(f'Неверное первое слово {word.split("-")[0]}')
                    copy_potential_nomenclature.remove(word)
                    continue
            except Exception:
                pass
            try:
                if word.split('-')[1] not in second_letter and word.split('-')[1] is not None:
                    print(f'Неверное второе слово {word.split("-")[1]}')
                    copy_potential_nomenclature.remove(word)
                    continue
            except Exception:
                pass
            try:
                if word.split('-')[2] not in third_letter and word.split('-')[2] is not None:
                    print(f'Неверное третье слово {word.split("-")[2]}')
                    copy_potential_nomenclature.remove(word)
                    continue
            except Exception:
                pass
            try:
                if word.split('-')[3] not in fourth_letter and word.split('-')[3] is not None:
                    print(f'Неверное четвертое слово {word.split("-")[3]}')
                    copy_potential_nomenclature.remove(word)
                    continue
            except Exception:
                pass
            try:
                if word.split('-')[4] not in fifth_letter and word.split('-')[4] is not None:
                    print(f'Неверное пятое слово {word.split("-")[4]}')
                    copy_potential_nomenclature.remove(word)
                    continue
            except Exception:
                pass
                for i in spec_symbols:
                    if i in word:
                        print(f'Запрещенный символ {i}')
                        copy_potential_nomenclature.remove(word)
                        break
            except Exception:
                pass
        potential_nomenclature = list(copy_potential_nomenclature)
        print(potential_nomenclature)
        if len(potential_nomenclature) != 0:
            return potential_nomenclature[-1]
        else:
            return None


def start_search(conf=None, q=None, r=None):
    """
    Инициализация модуля
    :param conf: значения конфигурационного файла
    :return: None
    """
    # time1 = time.time()
    if conf is None:
        conf = {}
    save_logging(conf=conf)

    tsrct.pytesseract.tesseract_cmd = conf['tesseract_path']
    path_of_maps = get_images_from_dir(conf['folder_with_maps'])
    target_folder = conf['target_folder']
    if path_of_maps is None or target_folder is None:
        save_logging(str=f'You need choose folder with maps and target folder\n')
        print(f'You need choose folder with maps and target folder\n')
        return

    height_of_head = int(conf['height_of_head'])
    lang = conf['lang']
    for path in path_of_maps:
        # print(time.time() - time1)
        # Подключение фото
        try:
            img = Image.open(path)
        except Exception:
            continue
        # Вычислим размер фото и шапки
        width, height = img.size
        height_head = int(height * height_of_head / 100)
        # Вырезаем шапку, в которой находится номенклатура
        img_cropped = img.crop((0, 0, width, height_head/4))
        # img_cropped.show()
        # Определяем текст на изображении
        # Лучше использовать rus+eng
        data_string = tsrct.image_to_string(img_cropped, lang=lang, config=config)
        img_cropped = img.crop((0, 0, width, height_head))
        # img_cropped.show()
        data_string2 = tsrct.image_to_string(img_cropped, lang=lang, config=config)
        data_string = data_string + data_string2
        # Листинг
        save_logging(str=f'{path_of_maps.index(path) + 1} / {len(path_of_maps)} | '
                         f'{((path_of_maps.index(path) + 1) / (len(path_of_maps)) * 100)}%')
        save_logging(str=f'{path}')
        save_logging(str=f'File {Path(path).name}')
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
            save_logging(str=f'Nomenclature is not found\n')
            continue
        else:
            file_name = f'{nomenclature}'
        i = 0
        while os.path.exists(target_folder+f'/{file_name}{rashirenie}'):
            i += 1
            if not os.path.exists(target_folder + f'/{file_name}({i}){rashirenie}'):
                file_name += f'({i})'

        shutil.copy(path, target_folder+f'/{file_name}{rashirenie}')
        # Обновляем прогресс бар
        q.put(((path_of_maps.index(path) + 1) / (len(path_of_maps)) * 100))
        r.event_generate('<<Updated>>', when='tail')
        # r.event_generate('<<Updated>>')
        save_logging(str=f'Saved as {target_folder}/{file_name}{rashirenie}\n')

    r.destroy()
    return


def update_progress_label(pb=None):
    if pb is None:
        return 'Current Progress: 0%'
    return f"Current Progress: {round(pb['value'], 2)}%"


def on_update(event, q=None, pb=None, value_label=None):
    # Получаем данные из очереди
    pb['value'] = q.get()
    value_label['text'] = update_progress_label(pb)


def init(conf):
    q = queue.Queue()
    root = tk.Tk()
    root.title("Поиск")
    root.geometry('300x50')
    value_label = ttk.Label(root, text=update_progress_label())
    value_label.pack()
    pb = ttk.Progressbar(root, mode="determinate")
    pb.pack()
    handler = partial(on_update, q=q, pb=pb, value_label=value_label)
    root.bind('<<Updated>>', handler)
    t = threading.Thread(target=start_search, args=(conf, q, root))
    t.start()
    root.mainloop()
    return
