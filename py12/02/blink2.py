from gpiozero import LED
from time import sleep

LED_PIN = 4
WAIT_TIME = 1

led = LED(LED_PIN)
count = 0
while count < 5:
   led.on()
   sleep(WAIT_TIME)
   led.off()
   sleep(WAIT_TIME)
   count += 1

