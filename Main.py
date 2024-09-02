import time
import board
import busio
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

time.sleep(1)
kit.servo[0].angle = 180
time.sleep(2)
kit.servo[1].angle = 180
time.sleep(2)
kit.servo[2].angle = 90
time.sleep(2)
kit.servo[3].angle = 90
time.sleep(2)
kit.servo[5].angle = 90
