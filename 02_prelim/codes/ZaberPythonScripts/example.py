from zaber_motion import Units
from zaber_motion import Library
from zaber_motion.ascii import Connection

Library.enable_device_db_store("./device-db-store")
with Connection.open_serial_port("COM3") as connection:
    device_list = connection.detect_devices()
    print("Found {} devices".format(len(device_list)))
    # The rest of your program goes here (indented)
    # indent this code under the "with" statement
    # device = device_list[0]
    #
    # axis = device.get_axis(1)
    # axis.home()
    # # indent this code under the "with" statement
    # # Move to the 10mm position
    # axis.move_absolute(10, Units.LENGTH_MILLIMETRES)
    # # Move by an additional 5mm
    # axis.move_relative(5, Units.LENGTH_MILLIMETRES)