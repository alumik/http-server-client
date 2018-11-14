from socket import AF_INET, SOCK_STREAM, socket, timeout
import sys
import threading


def main():
    server_socket = socket(AF_INET, SOCK_STREAM)
    host = 'localhost'
    server_port = 8080
    server_socket.bind((host, server_port))
    server_socket.listen(5)
    counter = 0

    print('Starting up http-server, serving ./')
    print('Available on:')
    print('  http://' + host + ':' + str(server_port))
    print('Hit CTRL-BREAK to stop the server')

    while True:
        connection_socket, address = server_socket.accept()
        counter += 1
        thread = threading.Thread(
            target=new_service,
            args=(connection_socket, address, counter)
        )
        thread.start()

    server_socket.close()
    sys.exit()


def new_service(connection_socket, address, counter):
    print('[#' + str(counter) + '] Connected by: ', address[0] + ':' + str(address[1]))

    try:
        connection_socket.settimeout(600)
        message = connection_socket.recv(1024).split()
        filename = message[1]
        print('[#' + str(counter) + '] Request: ', message[0].decode() + ' ' + message[1].decode())
        f = open(filename[1:], 'rb')
        output_data = f.read()
        connection_socket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
        connection_socket.send(output_data)
        connection_socket.send('\r\n'.encode())
    except IOError:
        connection_socket.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode())
        connection_socket.send('404 Not Found'.encode())
        connection_socket.send('\r\n'.encode())
    except IndexError:
        print('[#' + str(counter) + '] IndexError!')
    except timeout:
        print('[#' + str(counter) + '] Timeout!')
    except ConnectionResetError:
        print('[#' + str(counter) + '] ConnectionResetError!')
    finally:
        connection_socket.close()


if __name__ == '__main__':
    main()
