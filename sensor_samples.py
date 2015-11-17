#!/usr/bin/python

# sensor_samples.py
# Copyright (C) 2015 David L. Bennett <db42@hawaii.edu>
# for CS294: Python, Fall 2015, University of Hawaii at Hilo
#
# GitHub respository:
# https://github.com/muku42/initial-foray-into-raspberry-pi.git
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see: <http://www.gnu.org/licenses/>

###############
##
## This progam gives a small sampling of the sensor capability of the
## Raspberry Pi Sense Hat, also known as the AstroPi Hat. 
##
## Readings for temperature, relative humidity, and atmospheric pressure
## are taken and displayed via the terminal as well as the Sense Hat's
## 8x8 LED matrix.  Please keep in mind that the readings are taken directly
## at the Sense Hat.  Temperature for instance will be quite a bit higher than  
## the actual 'room' temperature because the Sense Hat is registering the heat
## produced by the Raspberry Pi itself.  Future setup will involve an extended
## female-to-male 40-pin GPIO connector to reduce the influence of the 
## Raspberry Pi itself.
##
###############

import time
from sense_hat import SenseHat

# Celscius to Fahrenheit
def c_to_f (t):
    result = (9.0/5.0) * t + 32
    return result

sense = SenseHat()
sense.clear() # clear the 8x8 matrix

tempC = sense.get_temperature()
tempC = round(tempC, 1)
tempF = c_to_f(tempC) # conversion from Celsius to Fahrenheit
tempF = round(tempF, 1)

print "The temperature at the Sense Hat is", tempC, "C or", tempF, "F"

sense.clear()

humidity = sense.get_humidity()
humidity = round(humidity, 1)

print "The relative humidity at the Sense Hat is", humidity, "%"

sense.clear()

pressure = sense.get_pressure()
pressure = round(pressure, 1)

print "The atmospheric pressure at the Sense Hat is", pressure, "mbar"

# outputing the temp, humidity, and pressure to the matrix

sense.clear()
sense.set_rotation(0) # sets orientation of Sense Hat matrix

# setting colors for the scrolling text on the matrix
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

speed = (0.06) # speed of text scroll (0.10 is default)
sleep = (0.6) # time of break in seconds

sense.show_message("Temp:", text_colour=red, scroll_speed=speed)
sense.show_message(str(tempC), text_colour=red, scroll_speed=speed)
sense.show_message("C", text_colour=red, scroll_speed=speed)
sense.show_message("or", text_colour=red, scroll_speed=speed)
sense.show_message(str(tempF), text_colour=red, scroll_speed=speed)
sense.show_message("F", text_colour=red, scroll_speed=speed)
time.sleep(sleep)
sense.show_message("Humidity:", text_colour=green, scroll_speed=speed)
sense.show_message(str(humidity), text_colour=green, scroll_speed=speed)
sense.show_message("%", text_colour=green, scroll_speed=speed)
time.sleep(sleep)
sense.show_message("Pressure:", text_colour=blue, scroll_speed=speed)
sense.show_message(str(pressure), text_colour=blue, scroll_speed=speed)
sense.show_message("mbar", text_colour=blue, scroll_speed=speed)

sense.clear()
