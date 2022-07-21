#!/usr/bin/env python3
# Path: Server\server.py

import socket
import threading
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(('0.0.0.0', 10000))

sock.listen(1)

connections = []

def handler(c, a):
    global connections
    while True:
        data = c.recv(1024)
        for connection in connections:
            connection.send(bytes(data))
        if not data:
            connections.remove(c)
            c.close()
            break

def send_message():
    while True:
        for connection in connections:
            connection.send(bytes('Connection Ping', 'utf-8'))
        time.sleep(10)


def log_connections():
    with open('connections.txt', 'w') as f:
        for connection in connections:
            f.write(str(time.time()) + connection.getpeername() + '\n')



while True:
    c, a = sock.accept()
    cThread = theading.Thread(target=handler, args=(c, a))
    cThread.daemon = True
    cThread.start()
    connections.append(c)
    print(f'Connection from {a[0]}')
    log_connections()
    send_message()
