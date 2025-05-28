import socket

def tcp_client():
    """Клиент подключается к серверу, отправляет сообщение и получает ответ"""
    host = "localhost"
    port = 9090

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))
            print("Подключено к серверу. Введите сообщение ('exit' для завершения).")

            while True:
                message = input("Введите сообщение: ")

                if message.lower() == "exit":
                    print("Закрытие соединения...")
                    break

                client_socket.sendall(message.encode('utf-8'))
                response = client_socket.recv(1024).decode('utf-8')
                print(f"Ответ сервера: {response}")

    except ConnectionRefusedError:
        print("Ошибка: сервер недоступен.")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    tcp_client()
