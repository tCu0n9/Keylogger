from pynput.mouse import Listener

def moveMouse(x,y):
    print('Position is: ({},{})'.format(x,y))

with Listener(on_move=moveMouse) as l:
    l.join()