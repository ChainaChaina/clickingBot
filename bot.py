from pyautogui import *
from random import *
import pyautogui
import time
import keyboard
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)    

def findButton(png):
    try:
        img = pyautogui.locateOnScreen(png, confidence=0.8, grayscale = True)
        click(img.left + 50, img.top + 25)
        return True
    except:
        return False

def checkClass():
    if findButton('invalidJson.png'):
        keyboard.press_and_release("f5")
        time.sleep(2)
    keyboard.press_and_release('page down')
    time.sleep(1.2)
    if findButton('completar.png'):
        time.sleep(0.5)
        findButton('proxima.png')

while keyboard.is_pressed('q') == False:
   checkClass()
