#! /usr/bin/env python

import serial, time, sys

if len(sys.argv) > 1:
    device = sys.argv[1]
else:
    device = "/dev/ttyACM0"

ser = serial.Serial(device, baudrate = 1200)
time.sleep(1.000)
ser.close()
