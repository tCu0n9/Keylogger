import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
machine = ""
port = 9999

server.bind((machine, port))
server.listen(5)

def receiver():
    print(f"[{machine}] Waiting for the connection from the client")
    while True:
        client, addr = server.accept()
        data = client.recv(1024)
        address = str(addr[0]).replace(".","-")
        with open(f"logOf{address}.txt", 'wb') as f:
            f.write(data)
            print(f"Received data from {addr}")

try:
    receiver()
except KeyboardInterrupt:
    pass