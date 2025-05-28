import socket

def start_echo_server():
    """Запускает TCP-сервер, принимающий сообщения и отправляющий их обратно клиенту"""
    host = "localhost"
    port = 9090

    try:
        # Создание TCP-сокета
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Позволяет повторное использование порта
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f"Сервер запущен на {host}:{port}. Ожидание подключений...")

        while True:
            conn, addr = server_socket.accept()
            print(f"Клиент подключен: {addr}")

            data = conn.recv(1024)
            if not data:
                break

            message = data.decode('utf-8')
            print(f"Получено сообщение от {addr}: {message}")

            if message.lower() == "shutdown":
                print("Получена команда shutdown. Завершение работы сервера.")
                conn.sendall("Сервер завершает работу.")
                conn.close()
                break

            conn.sendall(data)  # Эхо-ответ клиенту
            conn.close()

    except OSError as e:
        print(f"Ошибка сервера: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_echo_server()
