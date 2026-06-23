# =============

import mouse

import time  # using module time


draw_time = 1.8
recover = 2.5

while True:

    try:
        print('draw...')
        mouse.press("left")
        time.sleep(draw_time)
        print('fire!')
        mouse.release("left")
        time.sleep(recover)

    except:
        break

# =============
