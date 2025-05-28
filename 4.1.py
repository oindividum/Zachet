import os

# Запрос имени директории у пользователя
dir_name = input("Введите имя новой директории: ")

# Проверка существования директории
if os.path.exists(dir_name):
    print("Ошибка: Директория уже существует.")
else:
    try:
        # Создание директории
        os.makedirs(dir_name)
        # Создание файла info.txt с текстом
        file_path = os.path.join(dir_name, "info.txt")
        with open(file_path, "w") as file:
            file.write("New directory created")
        print(f"Директория '{dir_name}' успешно создана!")
    except Exception as e:
        print(f"Ошибка при создании директории: {e}")
