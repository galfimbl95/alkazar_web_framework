import socket
import threading
from time import sleep


def start_my_server():
    try:
        server = socket.socket()
        server.bind(('127.0.0.1', 2000))
        server.listen(10)
        client_socket, address = server.accept()
        while True:

            data = client_socket.recv(1024).decode('utf-8')
            print(data)
            # content = load_page_from_get_request(data)
            # client_socket.send(data)
            # client_socket.shutdown(socket.SHUT_WR)
    except KeyboardInterrupt:
        server.close()
        print('socket is closed')


def load_page_from_get_request(request_data):
    HDRS = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n"
    HDRS_404 = "HTTP/1.1 404 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n"
    path = request_data.split()[1]
    response = ''
    try:
        with open('views' + path, 'rb') as file:
            response = file.read()
        return HDRS.encode('utf-8') + response
    except FileNotFoundError:
        return (HDRS_404 + "Not found").encode('utf-8')

def start_my_client():
    while True:
        client_socket = socket.socket()
        client_socket.connect(("127.0.0.1", 2000))
        client_socket.send(b"Hello from client!")
        # client_socket.shutdown(socket.SHUT_WR)
        sleep(1)

start_my_server()


# if __name__ == "__main__":
#     srv_thread = threading.Thread(target=start_my_server)
#     srv_thread.start()
#     # client_thread = threading.Thread(target=start_my_client)
#     # client_thread.start()
