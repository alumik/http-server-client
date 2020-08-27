import sys
import threading

from socket import AF_INET, SOCK_STREAM, socket, timeout


def main():
    host, srv_port, www_root = get_config()
    srv_socket = socket(AF_INET, SOCK_STREAM)
    srv_socket.bind((host, srv_port))
    srv_socket.listen(5)
    con_number = 0

    print(f'Starting up http-server, serving ./{www_root}/')
    print('Available on:')
    print(f'  http://{host}:{srv_port}')
    print('Hit CTRL-BREAK to stop the server')

    while True:
        con_socket, address = srv_socket.accept()
        con_number += 1
        thread = threading.Thread(
            target=new_connection,
            args=(con_socket, address, con_number, www_root)
        )
        thread.start()


def get_config():
    args = sys.argv[1:]
    if not args:
        return 'localhost', 8080, 'web'
    return args[0], int(args[1]), args[2]


def new_connection(con_socket, address, con_number, www_root):
    print(f'[#{con_number}] Connected by: {address[0]}:{address[1]}')

    try:
        con_socket.settimeout(600)
        message = con_socket.recv(2048).decode().split()
        print(f'[#{con_number}] Request: {message[0]} {message[1]}')
        output_data = open(f'{www_root}/{message[1][1:]}', 'rb').read()

        con_socket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
        con_socket.send(output_data)
        con_socket.send('\r\n'.encode())
    except ConnectionResetError:
        print(f'[#{con_number}] ConnectionResetError!')
    except timeout:
        print(f'[#{con_number}] Timeout!')
    except IOError:
        con_socket.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode())
        con_socket.send('404 Not Found\r\n'.encode())
    except IndexError:
        print(f'[#{con_number}] IndexError!')
    finally:
        con_socket.close()


if __name__ == '__main__':
    main()
