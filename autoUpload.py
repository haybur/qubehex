#!/bin/env python3
import requests
import os
import filecmp
import time
from time import gmtime, strftime
import subprocess
import datetime
import pathlib

print("STARTING")

os.environ['TZ'] = 'EST+05EDT'
time.tzset()
starttime = time.time()

def getCode():
        url = "https://raw.githubusercontent.com/haybur/qubehex/main/qubecode.hex"
        #url = "https://raw.githubusercontent.com/haybur/qubehex/main/blink.hex"
        r = requests.get(url, allow_redirects=True, timeout=2.0)
        open('/home/pi/blink.hex', 'wb').write(r.content)

        file = pathlib.Path("/home/pi/blink.hex")
        if file.exists():
                os.rename("/home/pi/hex_output/blink.hex", "/home/pi/hex_output/blinkOld.hex")
                os.rename("/home/pi/blink.hex", "/home/pi/hex_output/blink.hex")
                sameFile = filecmp.cmp("/home/pi/hex_output/blink.hex", "/home/pi/hex_output/blinkOld.hex", shallow=False)
                with open("/home/pi/hex_output/blink.hex") as f:
                        first_line = f.readline().strip()
                        print(first_line)
                if sameFile:
                        print("same file, waiting 20 secs")
                        print(strftime("%a, %d %b %Y %H:%M:%S", time.localtime()))
                        #subprocess.call('./programTeensy blink.hex', shell=True)
                else:
                        print("different file, pushing code")
                        print(strftime("%a, %d %b %Y %H:%M:%S", time.localtime()))
                        subprocess.call('/home/pi/programTeensy blink.hex', shell=True)

        else:
                print("file not downloaded")

while True:
        print("running again")
        try:
                getCode()
                time.sleep(20)
        except:
                print("received error... trying again")
