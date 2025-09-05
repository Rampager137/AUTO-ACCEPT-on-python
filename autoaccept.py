import pyautogui
import time
import os
import sys

# Путь к изображению кнопки (указывай путь без русских букв)
image_path = r"E:\python projects\Prynyat igru(tolko prinyat).png"

# Проверяем, что файл который ты указал в переменной image_path существует
if not os.path.exists(image_path):
    print(f"Файл изображения не найден: {image_path}")
    sys.exit(1)

# max_attempts максимальное количество повторений программы(Программа повторяется каждую секунду)
max_attempts = 120
attempt = 0

while attempt < max_attempts:
    attempt += 1 # обычный счетчик повторений, именно это число пишется перед словом "Попытка" в CMD
    try:
        # Используем confidence (только с OpenCV)
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
