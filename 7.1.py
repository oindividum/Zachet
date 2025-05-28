import threading
import time

def task(name):
    """Симулирует выполнение задачи с паузой в 1 секунду"""
    print(f"Task {name} started")
    time.sleep(1)
    print(f"Task {name} finished")

# Список имен потоков
task_names = ["A", "B", "C"]

# Создание и запуск потоков
threads = []

for name in task_names:
    thread = threading.Thread(target=task, args=(name,))
    thread.start()
    threads.append(thread)

# Ожидание завершения всех потоков
for thread in threads:
    thread.join()

print("All tasks completed.")
