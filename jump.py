#=============

import keyboard # using module keyboard

import time # using module time



while True:

	try:

		keyboard.press_and_release('space')

		print('jump')

		time.sleep(1.33)
  
	except:

		break

#=============