import threading
import time

def task(name):
    print(f"Задача {name} началась")
    time.sleep(2)  # Имитация задержки
    print(f"Задача {name} завершена")

# Запуск 5 потоков
for i in range(5):
    t = threading.Thread(target=task, args=(f"Поток {i+1}",))
    t.start()
