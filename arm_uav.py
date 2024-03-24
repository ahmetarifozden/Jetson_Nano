#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
print "Start simulator (SITL)"
import dronekit_sitl
sitl = dronekit_sitl.start_default()
connection_string = sitl.connection_string()
"""
# Import DroneKit-Python
from dronekit import connect, VehicleMode
import time

//deneme gitlab

#iha = connect('/dev/ttyUSB0', wait_ready = True, baud = 115200)

#1. yöntem udp
iha = connect('udp:127.0.0.1:14551')

#2.yöntem tcp
#iha = connect('tcp:127.0.0.1:5762', wait_ready=True)


def arm():
	while iha.is_armable==False:
		print("Not ready to arm!")
		time.sleep(1)
	print("Ready to arm!")
	iha.mode    = VehicleMode("GUIDED")
	iha.armed=True
	while not iha.armed:
		print("Waiting for arming!")
		time.sleep(1)
	
	print("Drone armed")

	time.sleep(3)
	print("Mission is done!")

arm()
