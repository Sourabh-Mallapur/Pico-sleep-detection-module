# import machine
# import utime
# 
# # Define the pins
# x_pin = machine.ADC(26)
# y_pin = machine.ADC(27)
# z_pin = machine.ADC(28)
# 
# # Define the sensitivity factor (adjust as needed)
# sensitivity = 0.0033
# 
# while True:
#     # Read the raw values from the accelerometer pins
#     x_raw = x_pin.read_u16()
#     y_raw = y_pin.read_u16()
#     z_raw = z_pin.read_u16()
# 
#     # Convert the raw values to acceleration values in g-force
#     x_acc = 1.5+((x_raw >> 6) - 512) * sensitivity
#     y_acc = 1.5+((y_raw >> 6) - 512) * sensitivity
#     z_acc = 1.5+((z_raw >> 6) - 512) * sensitivity
# 
#     # Print the acceleration values
#     print("X: {:.2f}g, Y: {:.2f}g, Z: {:.2f}g".format(x_acc, y_acc, z_acc))
# 
#     # Delay for a short period of time
#     utime.sleep_ms(1000)

import machine
import utime
import ssd1306
from time import sleep

buzz = machine.Pin(25,machine.Pin.OUT)
buzz.low()

i2c = machine.SoftI2C(scl=machine.Pin(15), sda=machine.Pin(4))

pin = machine.Pin(16, machine.Pin.OUT)
pin.value(0) #set GPIO16 low to reset OLED
pin.value(1) #while OLED is running, must set GPIO16 in high

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# Define the pins
x_pin = machine.ADC(26)
y_pin = machine.ADC(27)
z_pin = machine.ADC(28)

# Define the sensitivity factor (adjust as needed)
sensitivity = 0.0033

# Define the motion threshold (adjust as needed)
motion_threshold = 2.4

# Define the time threshold for motion detection (in seconds)
motion_timeout = 1

# Initialize the last motion time
last_motion_time = utime.time()

while True:
    buzz.low()
    
    # Read the raw values from the accelerometer pins
    x_raw = x_pin.read_u16()
    y_raw = y_pin.read_u16()
    z_raw = z_pin.read_u16()

    # Convert the raw values to acceleration values in g-force
    x_acc = ((x_raw >> 6) - 512) * sensitivity
    y_acc = ((y_raw >> 6) - 512) * sensitivity
    z_acc = ((z_raw >> 6) - 512) * sensitivity

    # Calculate the magnitude of acceleration
    acceleration = (x_acc ** 2 + y_acc ** 2 + z_acc ** 2) ** 0.5
    print(acceleration)

    # Check if motion exceeds the threshold
    if acceleration < motion_threshold:
        last_motion_time = utime.time()
        oled.fill(0)
        oled.text("motion detected.", 0, 0)

    # Check if motion timeout has occurred
    if acceleration > motion_threshold or utime.time() - last_motion_time > motion_timeout:
        buzz.high()
        oled.fill(0)
        oled.text("No motion detected.", 0, 0)
    oled.show()

    # Delay for a short period of time
    utime.sleep_ms(1000)






