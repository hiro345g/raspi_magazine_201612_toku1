import gpiozero
import time

led = gpiozero.LED(4)
led.on()
time.sleep(3)
led.off()
