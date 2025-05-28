import os

def list_files_in_directory():
    # Запрашиваем путь к директории у пользователя
    dir_path = input("Введите путь к директории: ").strip()

    # Проверяем существование директории
    if not os.path.exists(dir_path):
        print("Directory not found")
        return

    # Получаем список файлов
    try:
        files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
        if files:
            print("Файлы в директории:")
            for file in files:
                print(file)
        else:
            print("В указанной директории нет файлов.")
    except Exception as e:
        print(f"Ошибка при обработке директории: {e}")

# Запускаем функцию
list_files_in_directory()
