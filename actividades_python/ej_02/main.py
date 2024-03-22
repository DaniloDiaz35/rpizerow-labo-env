from gpiozero import LED
from signal import pause

LED1 = LED(19)
LED2 = LED(13)
LED3 = LED(26)

LED1.blink(on_time=1, off_time=1, n=None, background=True)
LED2.blink(on_time=0.25, off_time=.25, n=None, background=True)
LED3.blink(on_time=0.5, off_time=.5, n=None, background=True)

pause()
