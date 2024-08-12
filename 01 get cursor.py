# install pyautogui by "pip install pyautogui" command, it'll ditect where our cursor is

import pyautogui

while True:
    a = pyautogui.position() 
    #Returns the current xy coordinates of the mouse cursor as a two-integer tuple.
    
    print(a)

