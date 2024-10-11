from Config.AntConfig import AntDeviceConfig
from HeadSensorController import HeadSensorController
from MotionController import MotionController

device_type = AntDeviceConfig.DATA_HUB

def main():
    print("Start main()")

    device = DataHub(AntDeviceConfig.DATA_HUB)
    device.run()


main()
