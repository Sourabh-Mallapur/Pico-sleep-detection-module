# Complete project details at https://RandomNerdTutorials.com

import machine
#from machine import Pin, SoftI2C
import ssd1306
from time import sleep

i2c = machine.SoftI2C(scl=machine.Pin(15), sda=machine.Pin(4))

pin = machine.Pin(16, machine.Pin.OUT)
pin.value(0) #set GPIO16 low to reset OLED
pin.value(1) #while OLED is running, must set GPIO16 in high

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.fill(0)
oled.text('Hello, World 1!', 0, 0)
oled.text('Hello, World 2!', 0, 10)
oled.text('Hello, World 3!', 0, 20)
oled.show()