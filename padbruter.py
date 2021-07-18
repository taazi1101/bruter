#Run as ROOT
import pyautogui
import keyboard
import time

i = 0
p = 0
limit_str = ""

def setup():
    us_aga = bool()
    enter = tuple()
    miscpos = []
    keypos = []
    keyspr = 0
    print("press k on top of all numbers in order 0-9.")
    while keyspr != 10:
        if keyboard.is_pressed("k"):
            keypos.append(pyautogui.position())
            keyspr += 1
            time.sleep(0.2)
    print("Press k on top of misc button(s) or press o to complete")
    keyspr = 0
    while True:
        if keyboard.is_pressed("k"):
            miscpos.append(pyautogui.position())
            keyspr += 1
            time.sleep(0.2)
        if keyboard.is_pressed("o"):
            break
    if len(miscpos) > 0:
        us_aga = True
    else:
        us_aga = False
    return keypos, miscpos, us_aga

print("Passcode lenght.")
amount = int(input(":"))

pyautogui.PAUSE = float(input("Delay:"))

for _ in range(0,amount):
    limit_str += "9"
limit = int(limit_str) + 1

print("1:Click | 2:Type")
if input(":") == "1":
    keyspos, again, us_aga = setup()
    print("press l to start and p to stop")
    while True:
        if keyboard.is_pressed("l"):
            for x in range(0,limit):
                x = str(x)
                if len(x) < amount:
                    p = amount - len(x)
                    x = "0"*p + x
                for y in str(x):
                    if keyboard.is_pressed("p"):
                        exit()
                    pyautogui.click(keyspos[int(y)])
                if us_aga:
                    for o in again:
                        pyautogui.click(o)
else:
    print("Press enter after each try? y/n")
    enterr = input(":")
    if enterr == "y":
        usen = True
    else:
        usen = False
    print("Press k on top of misc button(s) or press o to complete")
    keyspr = 0
    miscpos = []
    while True:
        if keyboard.is_pressed("k"):
            miscpos.append(pyautogui.position())
            keyspr += 1
            time.sleep(0.2)
        if keyboard.is_pressed("o"):
            break
    if len(miscpos) > 0:
        us_aga = True
    else:
        us_aga = False
    print("press l to start and p to stop")
    while True:
        if keyboard.is_pressed("l"):
            for x in range(0,limit):
                x = str(x)
                if len(x) < amount:
                    p = amount - len(x)
                    x = "0"*p + x
                for y in str(x):
                    if keyboard.is_pressed("p"):
                        exit()
                    pyautogui.press(y)
                if us_aga:
                    for j in miscpos:
                        pyautogui.click(j)
                if usen:
                    pyautogui.press("Enter")