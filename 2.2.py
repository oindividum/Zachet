import os


def list_directory():
    """Выводит список файлов и папок в текущей директории."""
    items = os.listdir()
    print("\nСодержимое текущей директории:")
    for item in items:
        print(item)


def create_directory(directory_name):
    """Создаёт новую папку в текущей директории, если она не существует."""
    try:
        if not os.path.exists(directory_name):
            os.mkdir(directory_name)
            print(f'Папка "{directory_name}" успешно создана.')
        else:
            print(f'Ошибка: папка "{directory_name}" уже существует.')
    except Exception as e:
        print(f'Ошибка при создании папки: {e}')


def main():
    """Основной цикл программы."""
    print("Текстовый файловый менеджер (работает в текущей директории)")
    print("Доступные команды: ls, mkdir <имя>, exit")

    while True:
        command = input("\nВведите команду: ").strip().split()

        if not command:
            continue

        if command[0] == "ls":
            list_directory()
        elif command[0] == "mkdir":
            if len(command) > 1:
                create_directory(command[1])
            else:
                print("Ошибка: необходимо указать имя папки.")
        elif command[0] == "exit":
            print("Выход из программы.")
            break
        else:
            print("Неизвестная команда. Доступные команды: ls, mkdir <имя>, exit.")


if __name__ == "__main__":
    main()
