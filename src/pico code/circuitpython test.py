import board
import busio
import adafruit_tsl2591
from time import sleep

i2c = busio.I2C(scl=board.GP1, sda=board.GP0)
# i2c = busio.I2C(board.SCL, board.SDA)

try:
    while True:
        sleep(1)
        sensor = adafruit_tsl2591.TSL2591(i2c)
        #sensor = adafruit_tsl2591.TSL2591(i2c)
        print('Light: {0}lux'.format(sensor.lux))
        print('Visible: {0}'.format(sensor.visible))
        print('Infrared: {0}'.format(sensor.infrared))

except KeyboardInterrupt:
    print("Stopped")

