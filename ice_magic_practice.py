# =============

import mouse

import time  # using module time


cast_time = 6
recover_time = 8

while True:

    try:
        print('cast!')
        mouse.press("left")
        time.sleep(cast_time)
        print('recover...')
        mouse.release("left")
        time.sleep(recover_time)

    except:
        break

# =============
