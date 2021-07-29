import zipfile
import os
import time

delay = float(0)
wordlist = ""
files = ""
info = """-f= : Path to zipfile
-w= : Path to wordlist
-d= : Delay"""

def rmdir(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    try:
        os.rmdir("zipTEMP-")
    except:
        pass

templ = []
os.sys.argv.pop(0)
for temp in os.sys.argv:
    temp.replace('"',"")
    templ.append(temp)

for arg in os.sys.argv:
    if "-w=" in arg:
        wordlist = arg.split("=")[1]
    elif "-f=" in arg:
        files = arg.split("=")[1]
    elif "-d=" in arg:
        delay = float(arg.split("=")[1])
    elif "-h" in arg:
        print(info)
        exit()
    else:
        print(f"Unknown argument: {arg}")

try:
    x = 1
    zip = zipfile.ZipFile(files,"r")
    with open(wordlist,"r") as infile:
        for line in infile:
            time.sleep(delay)
            line = line.replace("\n","")
            os.system("clear")
            print(f"[{str(x)}][{line}]")
            x += 1
            try:
                zip.extractall(path=f"zipTEMP-/",pwd=line.encode())
                print(f"Password : {line} | File : {files}")
            except:
                continue
            rmdir("zipTEMP-")
            exit()
    rmdir("zipTEMP-")
    print("Password not found.")
except:
    rmdir("zipTEMP-")
    exit()