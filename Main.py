import time
import board
import busio
import adafruit_pca9685
from adafruit_servokit import ServoKit
i2c = busio.I2C(board.SCL, board.SDA)
hat = adafruit_pca9685.PCA9685(i2c)
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
