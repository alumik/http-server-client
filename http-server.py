from socket import AF_INET, SOCK_STREAM, socket, timeout
import sys
import threading


def main():
    host, srv_port, www_root = get_config()
    srv_socket = socket(AF_INET, SOCK_STREAM)
    srv_socket.bind((host, srv_port))
    srv_socket.listen(5)
    con_number = 0

    print('Starting up http-server, serving ./' + www_root + '/')
    print('Available on:')
    print('  http://' + host + ':' + str(srv_port))
    print('Hit CTRL-BREAK to stop the server')

    while True:
        con_socket, address = srv_socket.accept()
        con_number += 1
        thread = threading.Thread(
            target=new_connection,
            args=(con_socket, address, con_number, www_root)
        )
        thread.start()

    srv_socket.close()
    sys.exit()


def get_config():
    args = sys.argv[1:]
    if not args:
        return 'localhost', 8080, 'www'
    return args[0], int(args[1]), args[2]


def new_connection(con_socket, address, con_number, www_root):
    print(
        '[#' + str(con_number) + '] ' +
        'Connected by: ' + address[0] + ':' + str(address[1])
    )

    try:
        con_socket.settimeout(600)
        message = con_socket.recv(2048).decode().split()
        print(
            '[#' + str(con_number) + '] ' +
            'Request: ' + message[0] + ' ' + message[1]
        )
        output_data = open(www_root + '/' + message[1][1:], 'rb').read()

        con_socket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
        con_socket.send(output_data)
        con_socket.send('\r\n'.encode())
    except ConnectionResetError:
        print('[#' + str(con_number) + '] ConnectionResetError!')
    except IOError:
        con_socket.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode())
        con_socket.send('404 Not Found\r\n'.encode())
    except IndexError:
        print('[#' + str(con_number) + '] IndexError!')
    except timeout:
        print('[#' + str(con_number) + '] Timeout!')
    finally:
        con_socket.close()


if __name__ == '__main__':
    main()
