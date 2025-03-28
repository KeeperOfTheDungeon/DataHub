from Config.AntConfig import AntDeviceConfig
from RoboControl.Robot.Device.Generic.DataHub.DataHub import DataHub
from DataHub import MotionController
from machine import UART, Pin
import time

def main():
    uart1 = UART(1, baudrate=115200, tx=Pin(4), rx=Pin(5), timeout=2000)
    print("Start main()")

    # device = MotionController(AntDeviceConfig.MAIN_DATA_HUB)
    # device.run()
    
    while True:
        time.sleep(0.001)
        if uart1.any():
            inpot = uart1.read(1)
            try: print(inpot.decode())
            except: print(inpot)
main()