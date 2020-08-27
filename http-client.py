import sys

from socket import AF_INET, SOCK_STREAM, socket


def main():
    cl_socket = socket(AF_INET, SOCK_STREAM)
    host, srv_port, filename = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    cl_socket.connect((host, srv_port))
    cl_socket.send(f'GET /{filename} HTTP/1.1\r\n\r\n'.encode())

    while True:
        data = cl_socket.recv(2048)
        if not data:
            break
        print(data.decode())

    cl_socket.close()


if __name__ == '__main__':
    main()
