import tkinter as tk
from tkinter import filedialog, ttk
import sys
import time, threading
from search_module import *

BUTTON_WIDTH = 40

# Значение по умолчанию конфигурационного файла
DEFAULT_CONFIG = {'tesseract_path': 'Tesseract-OCR/tesseract.exe',
                  'folder_with_maps': 'None',
                  'target_folder': 'None',
                  'lang': 'rus+eng',
                  'height_of_head': '8'}

CONFIG = {}

root = tk.Tk()
root.title("Поиск топографических карт")


def load_config():
    """
    Загрузка сохраненных на диске конфигурачионных настроек
    :return: Словарь с настройкми
    """
    CONFIG = {}
    with open('./config.ini', 'r') as inp:
        CONFIG = {}
        for line in inp:
            word = []
            word = line.split('=')
            word[1] = word[1].replace('\n', '')
            CONFIG.update([(word[0], word[1])])
    return CONFIG


def save_config(CONFIG):
    """
    Сохранение конфигурационных настроек на диск
    :param CONFIG: Словарь с настройками
    :return: None
    """
    with open('./config.ini', 'w') as inp:
        for i in CONFIG:
            inp.write(i + '=' + CONFIG.get(i) + '\n')
    return


def choose_folder_with_maps():
    """
    Выбор папки для поиска карт и сохранение ее пути в конфигурационном файле
    :return: None
    """
    try:
        directory_name = filedialog.askdirectory()
    except Exception:
        directory_name = ''
    if not isinstance(directory_name, str):
        sys.exit(1)
    if directory_name != '':
        CONFIG['folder_with_maps'] = directory_name
        save_config(CONFIG)
    return


def choose_target_folder():
    """
    Выбор целевой папки для переноса карт и сохранение ее пути в конфигурационном файле
    :return: None
    """
    try:
        directory_name = filedialog.askdirectory()
    except Exception:
        directory_name = ''
    if not isinstance(directory_name, str):
        sys.exit(1)
    if directory_name != '':
        CONFIG['target_folder'] = directory_name
        save_config(CONFIG)
    return


def choose_tesseract():
    """
    Выбор испольнительного файла tesseract-ocr
    :return: None
    """
    try:
        directory_name = filedialog.askopenfilename(filetypes=[('exe', '.exe')])
    except Exception:
        directory_name = ''
    if not isinstance(directory_name, str):
        sys.exit(1)
    if directory_name != '':
        CONFIG['tesseract_path'] = directory_name
        save_config(CONFIG)
    return


def launch():
    """
    Запуск модуля поиска
    :return: None
    """
    CONFIG = load_config()
    init(CONFIG)


if not os.path.exists('config.ini'):
    save_config(DEFAULT_CONFIG)
if not os.path.exists('logs.log'):
    with open('./logs.log', 'w') as inp:
        pass


CONFIG = load_config()
tk.Button(root, text="Запуск", width=BUTTON_WIDTH,
          command=lambda: launch()).pack()


# def progress():
#     pb['value'] = 10
#     # for i in range(20):
#     #     pb['value'] += i
#     #     time.sleep(.3)
#
#
# threading.Thread(target=progress).start()
tk.Button(root, text="Выбрать папку для поиска карт", width=BUTTON_WIDTH,
          command=lambda: choose_folder_with_maps()).pack()
tk.Button(root, text="Выбрать целевую папку", width=BUTTON_WIDTH,
          command=lambda: choose_target_folder()).pack()
tk.Button(root, text="Указать путь к Tesseract", width=BUTTON_WIDTH,
          command=lambda: choose_tesseract()).pack()
tk.Button(root, text="Установить настройки по умолчанию", width=BUTTON_WIDTH,
          command=lambda: save_config(DEFAULT_CONFIG)).pack()
tk.Button(root, text="Выход", width=BUTTON_WIDTH,
          command=lambda: root.destroy()).pack()
root.lift()

if __name__ == '__main__':
    root.mainloop()
