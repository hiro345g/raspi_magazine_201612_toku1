from gpiozero import LED
from time import sleep

LED_PIN = 4
WAIT_TIME = 1

led = LED(LED_PIN)
while True:
    led.on()
    sleep(WAIT_TIME)
    led.off()
    sleep(WAIT_TIME)

