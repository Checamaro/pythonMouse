import mouse
import time

# time.sleep(2)
# print(mouse.get_position())
# mouse.drag(1333, 752, 578, 422, duration=1)
# 1333 752
# 578 422

import pyautogui
import time
import random
import win32api, win32con

tab_counts = [1, 2, 3, 4, 5, 6, 7]

def move_mouse():
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    pyautogui.moveTo(x, y, duration=1)
    time.sleep(3)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y, 0, 0)

def alt_tab():
    win32api.keybd_event(0x12, 0, 0, 0)  # Alt
    win32api.keybd_event(0x09, 0, 0, 0)  # Tab
    for i in range(random.choice(tab_counts)):
        time.sleep(0.1)
        win32api.keybd_event(0x09, 0, 0, 0)  # Tab
        time.sleep(0.1)
    win32api.keybd_event(0x09, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(0x12, 0, win32con.KEYEVENTF_KEYUP, 0)

while True:
    move_mouse()
    alt_tab()
    time.sleep(random.randint(1, 7))