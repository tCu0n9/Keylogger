# test socket
import os
import socket
import time

def sender():
    machine = "127.0.0.1"
    port = 9999
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client.connect((machine, port))
        with open("log.txt", 'rb') as file:
            data = file.read(1024)
            while data:
                print("Sending data")
                client.send(data)
                data = file.read(1024)
            print("Data sent successfully")
    except Exception as e:
        print(f"Failed to send data: {e}")
    finally:
        client.close()

sender()