import os
import sys
import ctypes
import webbrowser

# Проверка прав администратора
def есть_права_администратора():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not есть_права_администратора():
    print("Запрос прав администратора.")
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

# Функции поиска
def search_google():
    query = input("Введите запрос для поиска в Google: ")
    url = f'https://www.google.com/search?q={query}'
    webbrowser.open(url)

def search_bing():
    query = input("Введите запрос для поиска в Bing: ")
    url = f'https://www.bing.com/search?q={query}'
    webbrowser.open(url)

def search_yandex():
    query = input("Введите запрос для поиска в Яндексе: ")
    url = f'https://yandex.ru/search/?text={query}'
    webbrowser.open(url)

# Функция калькулятора
def calculator():
    print("Калькулятор. Введите выражение (например, 2 + 3 * 4):")
    expr = input(">>> ")
    try:
        result = eval(expr, {'__builtins__': None}, {})
        print(f"Результат: {result}")
    except Exception as e:
        print(f"Ошибка при вычислении: {e}")

# Основное меню
def главное_меню():
    while True:
        # Установка цвета и заголовка (опционально)
        try:
            os.system('color 1E')
        except:
            pass
        try:
            os.system('title MrMarkYT (TM)')
        except:
            pass

        print("\n===== MarkRu Tools + Игры =====")
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
        print("13. Играть: Угадай число")
        print("14. Играть: Гонка на мотоцикле")
        print("15. Играть: Крестики-нолики")
        print("16. Создать файл")
        print("17. Удалить файл")
        print("0. Выйти")

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
            os.system("taskmgr")
        elif choice == '6':
            os.system("del %TEMP%\\* /Q /F")
            print("Папка TEMP очищена.")
        elif choice == '7':
            os.system("shutdown /r /t 60")
            print("Перезагрузка через 1 минуту initiated.")
        elif choice == '8':
            os.system("shutdown /s /t 60")
            print("Выключение через 1 минуту initiated.")
        elif choice == '9':
            os.system("shutdown /a")
            print("Отмена перезагрузки/выключения.")
        elif choice == '10':
            change_window_color()
        elif choice == '11':
            os.system("shutdown /r /f /t 0")
        elif choice == '12':
            os.system("shutdown /s /f /t 0")
        elif choice == '13':
            игра_угадай_число()
        elif choice == '14':
            гонка_на_мотоцикле()
        elif choice == '15':
            игра_крестики_нолики()
        elif choice == '16':
            создать_файл()
        elif choice == '17':
            удалить_файл()
        elif choice == '0':
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

# Реализация игр и дополнительных функций (примеры)
import random

def игра_угадай_число():
    number = random.randint(1, 50)
    print("Я загадал число от 1 до 50. Попробуйте угадать!")
    while True:
        try:
            guess = int(input("Ваш ответ: "))
            if guess == number:
                print("Поздравляю! Вы угадали!")
                break
            elif guess < number:
                print("Меньше.")
            else:
                print("Больше.")
        except:
            print("Пожалуйста, введите число.")

def гонка_на_мотоцикле():
    print("Error -1291 Дополнительный пакет для игры не загружен! ")
    # Можно добавить реализацию по желанию

def игра_крестики_нолики():
    print("Игра 'Крестики-нолики':")
    board = [' ']*9

    def print_board():
        print(f"{board[0]}|{board[1]}|{board[2]}")
        print("-+-+-")
        print(f"{board[3]}|{board[4]}|{board[5]}")
        print("-+-+-")
        print(f"{board[6]}|{board[7]}|{board[8]}")

    def check_win(player):
        wins = [(0,1,2), (3,4,5), (6,7,8),
                (0,3,6), (1,4,7), (2,5,8),
                (0,4,8), (2,4,6)]
        return any(all(board[i] == player for i in combo) for combo in wins)

    current_player = 'X'
    for _ in range(9):
        print_board()
        move = input(f"Игрок {current_player}, ваш ход (0-8): ")
        try:
            move = int(move)
            if board[move] == ' ':
                board[move] = current_player
                if check_win(current_player):
                    print_board()
                    print(f"Игрок {current_player} выиграл!")
                    return
                current_player = 'O' if current_player=='X' else 'X'
            else:
                print("Это поле уже занято.")
        except:
            print("Некорректный ввод.")
    print_board()
    print("Ничья!")

# Функции для работы с файлами
def создать_файл():
    dir_path = input("Введите путь к директории для создания файла: ")
    filename = input("Введите имя файла (например, myfile.txt): ")
    full_path = os.path.join(dir_path, filename)
    content = input("Введите содержимое файла: ")
    try:
        os.makedirs(dir_path, exist_ok=True)
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Файл {full_path} успешно создан.")
    except Exception as e:
        print(f"Ошибка при создании файла: {e}")

def удалить_файл():
    dir_path = input("Введите путь к директории: ")
    filename = input("Введите имя файла для удаления: ")
    full_path = os.path.join(dir_path, filename)
    try:
        if os.path.exists(full_path):
            os.remove(full_path)
            print(f"Файл {full_path} успешно удален.")
        else:
            print("Файл не найден.")
    except Exception as e:
        print(f"Ошибка при удалении файла: {e}")

# Меню изменение цвета окна
def change_window_color():
    print("Доступные цвета:")
    print("1. Синий")
    print("2. Зеленый")
    print("3. Красный")
    print("4. Белый")
    choice = input("Выберите цвет (1-4): ")
    color_codes = {'1':'1E', '2':'2E', '3':'4E', '4':'0F'}
    if choice in color_codes:
        os.system(f'color {color_codes[choice]}')
    else:
        print("Некорректный выбор.")

def main():
    # Открываем приветственный HTML
    webbrowser.open('file:///C:/MarkRuTools/welcome.html')
    главное_меню()

if __name__ == "__main__":
    main()

