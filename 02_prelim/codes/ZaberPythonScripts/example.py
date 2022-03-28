from zaber_motion import Units
from zaber_motion import Library
from zaber_motion.ascii import Connection

Library.enable_device_db_store("./device-db-store")
# This is an example script that instructs the device to perform two movements, with a specified velocity
with Connection.open_serial_port("COM3") as connection:
    device_list = connection.detect_devices()
    print("Found {} devices".format(len(device_list)))
    # The rest of your program goes here (indented)
    # indent this code under the "with" statement
    device = device_list[0]
    axis = device.get_axis(1)
    axis.home()
    # indent this code under the "with" statement
    # Begins to move axis at specified speed. LINE BELOW NOT TESTED WITH ZABER STAGE
    axis.move_velocity(3, unit=Units.VELOCITY_MILLIMETRES_PER_SECOND)
    # Move to the 10mm position
    axis.move_absolute(10, Units.LENGTH_MILLIMETRES)
    # Move by an additional 5mm
    axis.move_relative(5, Units.LENGTH_MILLIMETRES)
