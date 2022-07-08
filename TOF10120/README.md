This library is for TOF10120 time of flight distance measurement module.

Tested by using the ESP32 development board.

Usage:

import tof10120

tof = tof10120.TOF10120(scl_pin, sda_pin)

distance = tof.measure()

print(distance)
