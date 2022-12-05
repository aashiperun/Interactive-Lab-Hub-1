import time
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
# There are 16 channels on the PCA9685 chip.
kit = ServoKit(channels=16)

# Name and set up the servo according to the channel you are using.
servo1 = kit.servo[0]
servo2 = kit.servo[1]
servo3 = kit.servo[2]
servo4 = kit.servo[3]

# Set the pulse width range of your servo for PWM control of rotating 0-180 degree (min_pulse, max_pulse)
# Each servo might be different, you can normally find this information in the servo datasheet
servo1.set_pulse_width_range(500, 2500)
servo2.set_pulse_width_range(500, 2500)
servo3.set_pulse_width_range(500, 2500)
servo4.set_pulse_width_range(500, 2500)
t=1
while t!=0:
    try:
        # Set the servo to 180 degree position
        servo1.angle = 180
        time.sleep(0.1)
        # Set the servo to 0 degree position
        servo1.angle = 0
        time.sleep(0.1)
        t-=1
        # Set the servo to 180 degree position 
        servo2.angle = 180
        time.sleep(0.1)
        # Set the servo to 0 degree position
        servo2.angle = 0
        time.sleep(0.1)

        # Set the servo to 180 degree position
        servo3.angle = 180
        time.sleep(0.1)
        # Set the servo to 0 degree position
        servo3.angle = 0
        time.sleep(0.1)

        # Set the servo to 180 degree position
        servo4.angle = 180
        time.sleep(0.1)
        # Set the servo to 0 degree position
        servo4.angle = 0
        time.sleep(0.1)
        
    except KeyboardInterrupt:
        # Once interrupted, set the servo back to 0 degree position
        servo1.angle = 0
        servo2.angle = 0
        servo3.angle = 0
        servo4.angle = 0
        time.sleep(0.5)
        break
