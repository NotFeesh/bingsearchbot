import time
import pyautogui
import random
import keyboard

word_file = open('words.txt', 'r')
words = word_file.read()

print("Press ENTER to start after you tab into Edge")
keyboard.wait('enter')

print("Completing Desktop Search Rewards...")

pyautogui.hotkey('ctrl', 't')

# Desktop Rewards
for x in range(34):
    pyautogui.hotkey('alt', 'd')
    search_length = random.randint(1, 4)
    for y in range(search_length):
        pyautogui.typewrite(f"{words[random.randint(0, words.length - 1)]} ")
    pyautogui.keyDown('enter')
    print(x, "/34")
    time.sleep(6)

print("Finished Desktop Search Rewards.")

print("Completing Mobile Search Rewards...")

# Mobile Rewards
pyautogui.hotkey('ctrl', 'shift', 'i')
time.sleep(random.random() * 5)

for x in range(20):
    pyautogui.hotkey('alt', 'd')
    search_length = random.randint(1, 4)
    for y in range(search_length):
        pyautogui.typewrite(f"{words[random.randint(0, words.length - 1)]} ")
    pyautogui.keyDown('enter')
    print(x, "/20")
    time.sleep(6)

print("Finished Mobile Search Rewards.")
