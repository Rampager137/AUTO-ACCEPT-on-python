import pyautogui
import time
import os
import sys

# Папка, где лежит этот скрипт
script_dir = os.path.dirname(os.path.abspath(__file__))

# Имя файла с кнопкой
image_file = "Prynyat igru(tolko prinyat).png"

# Полный путь к картинке
image_path = os.path.join(script_dir, image_file)

# Проверяем, что файл существует
if not os.path.exists(image_path):
    print(f"Файл изображения не найден: {image_path}")
    sys.exit(1)

# Максимальное количество попыток
max_attempts = 600
attempt = 0

while attempt < max_attempts:
    attempt += 1
    try:
        # Поиск кнопки на экране (confidence работает только с OpenCV)
        location = pyautogui.locateOnScreen(image_path, confidence=0.8)
        if location:
            pyautogui.click(pyautogui.center(location))
            print("Игра подтверждена!")
            break
        else:
            print(f"Попытка {attempt}: кнопка не найдена")
    except Exception:
        print(f"{attempt} секунд, поиск идет")

    time.sleep(1)
else:
    print("Не удалось найти кнопку за отведённое количество попыток")

