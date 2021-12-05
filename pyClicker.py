#pyClicker
#Filip Rokita
#www.filiprokita.com

import time
import pyautogui
import keyboard

startButton = input("START BUTTON: ")
stopButton = input("STOP BUTTON: ")

while True:
    if keyboard.is_pressed(startButton) == True:
        while True:
            pyautogui.click()
            if keyboard.is_pressed(stopButton) == True:
                break