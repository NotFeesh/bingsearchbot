import time
import pyautogui
import random
import keyboard

word_file = open('words.txt', 'r')
words = word_file.readlines()

def randomSearch(repeat):
  for x in range(repeat):
    pyautogui.hotkey('alt', 'd')
    pyautogui.typewrite(f"{words[random.randint(0, len(words) - 1)]} ")
    pyautogui.keyDown('enter')
    print(x, f"/{str(repeat)}")
    time.sleep(6)

print("Press ENTER to start after you tab into Edge")
keyboard.wait('enter')

print("Completing Desktop Search Rewards...")

pyautogui.hotkey('ctrl', 't')

# Desktop Rewards
randomSearch(34)

print("Finished Desktop Search Rewards.")

print("Completing Mobile Search Rewards...")

# Mobile Rewards
pyautogui.hotkey('ctrl', 'shift', 'i')
randomSearch(20)

print("Finished Mobile Search Rewards.")
