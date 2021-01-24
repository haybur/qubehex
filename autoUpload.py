import requests
import os
import filecmp
import time
from time import gmtime, strftime
import subprocess
import datetime

print("STARTING")

os.environ['TZ'] = 'EST+05EDT'
time.tzset()
starttime = time.time()

def getCode():
	url = "https://raw.githubusercontent.com/haybur/qubehex/main/blink.hex"
	r = requests.get(url, allow_redirects=True)
	open('blink.hex', 'wb').write(r.content)

	os.rename("/home/pi/hex_output/blink.hex", "/home/pi/hex_output/blinkOld.hex")
	os.rename("/home/pi/blink.hex", "/home/pi/hex_output/blink.hex")
	sameFile = filecmp.cmp("/home/pi/hex_output/blink.hex", "/home/pi/hex_output/blinkOld.hex", shallow=False)
	with open("/home/pi/hex_output/blink.hex") as f: 
		first_line = f.readline().strip()
		print(first_line)
#	for l in f.readline():
        #		print(l)
	if sameFile:
		print("same file, waiting 20 secs")
		print(strftime("%a, %d %b %Y %H:%M:%S", time.localtime()))
		#subprocess.call('./programTeensy blink.hex', shell=True)
	else:
		print("different file, pushing code")
		print(strftime("%a, %d %b %Y %H:%M:%S", time.localtime()))
		subprocess.call('./programTeensy blink.hex', shell=True)


while True:
	print("running again")
	getCode()
	time.sleep(20)
