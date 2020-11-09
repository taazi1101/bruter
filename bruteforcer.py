import pyautogui
import keyboard
from time import sleep
print("Wordlist")
wordlist = input(":")
print("use enter?")
print("yes:1 no:2")
enter = input(":")
print("Select cooldown  {has to be a float}")
cooldown = float(input(""))
pyautogui.PAUSE = cooldown


print("Strating in 5 seconds")
sleep(5)
print("start!")
if wordlist.endswith('.txt'):
    if enter == '1':
        with open(wordlist) as f:
            print("pause by pressing 'q'")
            for line in f:
                if keyboard.is_pressed('q'):
                    print("Exit")
                    exit()
                else:
                    pyautogui.typewrite(line)
                    pyautogui.press('enter')
    if enter == '2':
        with open(wordlist) as f:
            print("pause by pressing 'q'")
            for line in f:
                if keyboard.is_pressed('q'):
                    print("Exit")
                    exit()
                else:
                    pyautogui.typewrite(line)

    else:
        print("Invalid input")
else:
    print("Invalid file extension")