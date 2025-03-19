from Config.AntConfig import AntDeviceConfig
from RoboControl.Robot.Device.Generic.DataHub.DataHub import DataHub

def main():
    print("Start main()")

    device = DataHub(AntDeviceConfig.MAIN_DATA_HUB)
    device.run()


main()
