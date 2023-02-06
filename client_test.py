import socket
import threading

import config


def receiving():
    global receiving_data
    while True:
        receiving_data += client.recv(1024).decode('ascii')
        print(receiving_data)


def write():
    while True:
        message = input()

        if message == 'close':
            client.close()

        message = nickname + ': ' + message + '\n'
        client.send(message.encode('ascii'))


client = socket.socket()
client.connect(config.socket)

nickname = 'Test'
client.send(nickname.encode('ascii'))

receiving_data = ''

receiving_thread = threading.Thread(target=receiving).start()
write_thread = threading.Thread(target=write).start()
