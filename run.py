#=============
import keyboard # using module keyboard
import time # using module time

while True:
	try:
		keyboard.press('shift')
		print('pressed shift')
		time.sleep(15.0)
		keyboard.release('shift')
		print('released shift')
		time.sleep(3.0)
	except:
		break
#=============