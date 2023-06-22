import machine
import utime

# Define the analog input pin
analog_pin = machine.ADC(26)

# Constants for sleep detection
sleep_threshold = 60  # Adjust this threshold based on your observations
sleep_duration = 5000  # Adjust this duration based on your requirements (in milliseconds)

# Variables for sleep detection
prev_time = utime.ticks_ms()
sleeping = False

while True:
    # Read the analog value from the sensor
    value = analog_pin.read_u16()

    # Check for a heartbeat
    if value > prev_value:
        current_time = utime.ticks_ms()
        time_diff = current_time - prev_time

        # Calculate heart rate in beats per minute (BPM)
        heart_rate = 60000 / time_diff  # Assuming time_diff is in milliseconds

        # Check if heart rate is below the sleep threshold
        if heart_rate < sleep_threshold:
            if not sleeping:
                sleeping = True
                print("Sleeping")
        else:
            if sleeping:
                sleeping = False
                print("Waking up")

        prev_time = current_time

    # Update the previous value
    prev_value = value

    # Delay for a short period
    utime.sleep_ms(10)