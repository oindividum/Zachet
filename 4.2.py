import os

# Получение текущего рабочего каталога
current_directory = os.getcwd()
print(f"Текущий каталог: {current_directory}")

# Получение переменной окружения PATH
path_variable = os.environ.get('PATH')

# Проверка наличия переменной PATH и вывод результата
if path_variable:
    print(f"Значение переменной PATH:\n{path_variable}")
else:
    print("PATH not found")
