from socket import AF_INET, SOCK_STREAM, socket
import sys


def main():
    client_socket = socket(AF_INET, SOCK_STREAM)
    host = sys.argv[1]
    server_port = int(sys.argv[2])
    filename = sys.argv[3]
    client_socket.connect((host, server_port))
    client_socket.send(('GET /' + filename + ' HTTP/1.1\r\n\r\n').encode())

    while True:
        data = client_socket.recv(2048)
        if not data:
            break
        print(data.decode())

    client_socket.close()


if __name__ == '__main__':
    main()
