import time
import pyautogui
import random
import keyboard

print("Press ENTER to start after you tab into Edge")
keyboard.wait('enter')

print("Completing Desktop Search Rewards...")

pyautogui.hotkey('ctrl', 't')

# Desktop Rewards
for x in range(34):
    pyautogui.hotkey('alt', 'd')
    pyautogui.typewrite(str(random.random()))
    pyautogui.keyDown('enter')
    print(x, "/34")
    time.sleep(random.random() * 5)

print("Finished Desktop Search Rewards.")

print("Completing Mobile Search Rewards...")

# Mobile Rewards
pyautogui.hotkey('ctrl', 'shift', 'i')
time.sleep(random.random() * 5)

for x in range(20):
    time.sleep(random.random() * 5)
    pyautogui.hotkey('alt', 'd')
    pyautogui.typewrite(str(random.random()))
    pyautogui.keyDown('enter')
    print(x, "/20")

print("Finished Mobile Search Rewards.")
