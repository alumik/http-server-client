from socket import *
import sys

server_socket = socket(AF_INET, SOCK_STREAM)
host = 'localhost'
server_port = 8080
server_socket.bind((host, server_port))
server_socket.listen(5)

print('Starting up http-server, serving ./')
print('Available on:')
print('  http://' + host + ':' + str(server_port))
print('Hit CTRL-BREAK to stop the server')

while True:
    connection_socket, address = server_socket.accept()
    print()
    print('Connected by: ', address[0] + ':' + str(address[1]))

    try:
        message = connection_socket.recv(1024)
        filename = message.split()[1]
        print('Filename to get: ', filename[1:].decode())
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
        print('IndexError!')
    finally:
        connection_socket.close()

server_socket.close()
sys.exit()
