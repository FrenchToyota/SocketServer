from time import thread_time
import server

def connection():
    s = server.socket(server.AF_INET, server.SOCK_STREAM)
    s.connect((server.HOST, server.PORT))
    s.send(bytes('Connection Ping', 'utf-8'))
    while True:
        data = s.recv(1024)
        if not data:
            break
        print(data.decode('utf-8'))
        s.send(bytes(data))

def thread_connection():
    t = threading.Thread(target=connection)
    t.daemon = True
    t.start()


thread_connection()



