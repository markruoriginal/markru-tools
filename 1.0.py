import webbrowser
import os
import subprocess
import sys
import ctypes
import urllib.parse
import json

# Словарь цветов Windows CLI (цветовая комбинация: описание)
colors = {
    '0': 'Черный',
    '1': 'Синий темный',
    '2': 'Зеленый темный',
    '3': 'Бирюзовый темный',
    '4': 'Кнопка темная',
    '5': 'Пурпурный темный',
    '6': 'Желто-зеленый',
    '7': 'Светлый серый',
    '8': 'Серый',
    '9': 'Голубой',
    'A': 'Зеленый',
    'B': 'Бирюзовый',
    'C': 'Красный',
    'D': 'Розовый',
    'E': 'Желтый',
    'F': 'Белый'
}

def change_window_color():
    print("Доступные цвета:")
    for code, desc in colors.items():
        print(f"{code}: {desc}")
    color_code = input("Введите код цвета, чтобы установить (например, A): ").upper()
    if color_code in colors:
        os.system(f'color {color_code}')
        print(f"Цвет окна изменен на {colors[color_code]}.")
    else:
        print("Недопустимый код цвета.")

# Остальные функции-заглушки, которые должны быть реализованы
def search_google():
    query = input("Введите поисковый запрос для Google: ")
    os.system(f'start https://google.com/search?q={query}')

def search_bing():
    query = input("Введите поисковый запрос для Bing: ")
    os.system(f'start https://bing.com/search?q={query}')

def search_yandex():
    query = input("Введите поисковый запрос для Yandex: ")
    os.system(f'start https://yandex.ru/search/?text={query}')

def calculator():
    try:
        expression = input("Введите выражение для вычисления: ")
        result = eval(expression)
        print(f"Результат: {result}")
    except Exception as e:
        print(f"Ошибка вычисления: {e}")

def open_task_manager():
    os.system("taskmgr")  # Только для Windows

def clean_temp_folder():
    temp_dir = os.getenv('TEMP')
    if temp_dir:
        for filename in os.listdir(temp_dir):
            file_path = os.path.join(temp_dir, filename)
            try:
                os.remove(file_path)
            except Exception as e:
                print(f"Не удалось удалить {file_path}: {e}")
        print("Папка TEMP очищена.")
    else:
        print("Невозможно определить папку TEMP.")

def reboot_in_one_minute():
    os.system('shutdown /r /t 60')

def shutdown_in_one_minute():
    os.system('shutdown /s /t 60')

def cancel_shutdown():
    os.system('shutdown /a')

def reboot_computer():
    if sys.platform.startswith('win'):
        os.system('shutdown /r /t 0')
        print("Перезагрузка выполнена.")
    else:
        print("Эта команда работает только в Windows.")

def shutdown_computer():
    if sys.platform.startswith('win'):
        os.system('shutdown /s /t 0')
        print("Выключение выполнено.")
    else:
        print("Эта команда работает только в Windows.")

def main_menu():
    """Главное меню - выбор действий Пользователя."""
    while True:
        # Установка цвета и заголовка
        try:
            os.system('color 1E')
        except:
            pass
        try:
            os.system('title MrMarkYT (TM)')
        except:
            pass

        print("\n===== MarkRu Tools =====")
        print("Главное меню:")
        print("1. Поисковик Google.com")
        print("2. Поисковик bing.com")
        print("3. Поисковик yandex.ru")
        print("4. Режим калькулятора")
        print("5. Запустить TaskMgr (Windows)")
        print("6. Очистить папку TEMP")
        print("7. Перезагрузить компьютер через 1 минуту")
        print("8. Выключить компьютер через 1 минуту")
        print("9. Отменить перезагрузку/выключение")
        print("10. Изменить цвет окна")
        print("11. Перезагрузить компьютер сейчас")
        print("12. Выключить компьютер сейчас")
        print("0. Выйти")  # последний пункт

        choice = input("Выберите опцию: ")

        if choice == '1':
            search_google()
        elif choice == '2':
            search_bing()
        elif choice == '3':
            search_yandex()
        elif choice == '4':
            calculator()
        elif choice == '5':
            open_task_manager()
        elif choice == '6':
            clean_temp_folder()
        elif choice == '7':
            reboot_in_one_minute()
        elif choice == '8':
            shutdown_in_one_minute()
        elif choice == '9':
            cancel_shutdown()
        elif choice == '10':
            change_window_color()
        elif choice == '11':
            reboot_computer()
        elif choice == '12':
            shutdown_computer()
        elif choice == '0':
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

# Запуск меню
if __name__ == "__main__":
    main_menu()

