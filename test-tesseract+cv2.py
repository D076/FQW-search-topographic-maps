import pytesseract
import cv2
import os


def get_images_from_dir(folder='maps'):
    path_ = []
    for root, dirs, files in os.walk(folder):
        for filename in files:
            if filename.lower().endswith(('.jpg', '.gif', '.png', '.jpeg', '.tif', '.bmp')):
                print(root+'\\'+filename)
                path_.append(root+'\\'+filename)
    return path_


# показ изображения при cv2
def view_image(image, name_of_window='Something'):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
percent_of_head = 8  # Высота шапки в % (примерно 8)
config = r'--oem 3 --psm 6'  # Конфигурация tesseract
folder_with_maps = 'maps'
path_of_maps = get_images_from_dir(folder_with_maps)

# cv2
# ToDo cv2 при открытии файла с русскими символами возникает ошибка
# Подключение фото
img = cv2.imread(path_of_maps[0])
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# Вычислим размер фото и шапки
height = img.shape[0]
width = img.shape[1]
height_head = int(height * percent_of_head / 100)
# Вырезаем шапку
img = img[0:height_head, 0:width]
view_image(img)


# Определяем текст на изображении
print(pytesseract.image_to_string(img, lang='rus+eng', config=config))
# data = pytesseract.image_to_data(img, lang='rus+eng', config=config)
# print(data)
