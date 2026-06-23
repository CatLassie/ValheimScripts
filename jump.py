#=============

import keyboard # using module keyboard

import time # using module time



while True:

	try:

		# keyboard.press_and_release('space')

		keyboard.press("space")
		time.sleep(0.15)
		keyboard.release("space")

		print('jump')

		time.sleep(1.66)
  
	except:

		break

#=============