import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
machine = ""
port = 9999
i = 0

server.bind((machine, port))
server.listen()

def receiver():
    global i
    print(f"[{machine}] Waiting for the connection from the client")
    while True:
        client, addr = server.accept()
        data = client.recv(1024)
        with open("log1.txt", 'wb') as f:
            f.write(data)
            print(f"Received data from {addr}")
            i+=1

receiver()