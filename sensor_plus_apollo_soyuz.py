# sensor_plus_apollo_soyuz.py
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
## After the sensors finish taking their readings and displaying the results
## via the matrix, the Apollo-Soyuz model is rendered and displayed on screen
## with the IMU of the Sense Hat controlling the animated model and its pitch,
## roll, & yaw.
##
###############

#!/usr/bin/python

import time
import math
import pi3d
from sense_hat import SenseHat

# Celscius to Fahrenheit
def c_to_f(t):
    result = (9.0/5.0) * t + 32
    return result

def sensors():
    sense = SenseHat()

    tempC = sense.get_temperature() # obtains temperature in Celsius from sensor
    tempC = round(tempC, 1)
    tempF = c_to_f(tempC) # conversion from Celsius to Fahrenheit
    tempF = round(tempF, 1)

    print "The temperature at the Sense Hat is", tempC, "C or", tempF, "F"

    humidity = sense.get_humidity()
    humidity = round(humidity, 1)

    print "The relative humidity at the Sense Hat is", humidity, "%"

    pressure = sense.get_pressure()
    pressure = round(pressure, 1)

    print "The atmospheric pressure at the Sense Hat is", pressure, "mbar"

    # outputing the temp, humidity, and pressure to the matrix
    sense.clear() # clear the 8x8 matrix
    sense.set_rotation(0) # sets orientation of Sense Hat matrix

    # setting colors for the scrolling text on the matrix
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

    speed = (0.06) # speed of text scroll (0.10 is default)
    sleep = (0.6) # time of pause in seconds

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

def pi3d_model():

    display = pi3d.Display.create()
    cam = pi3d.Camera.instance()

    shader = pi3d.Shader("mat_light")

    model = pi3d.Model(
        file_string="apollo-soyuz.obj",
        name="model", x=0, y=-1, z=40, sx=1.75, sy=1.75, sz=1.75)

    model.set_shader(shader)

    cam.position((0, 20, 0))
    cam.point_at((0, -1, 40))
    keyb = pi3d.Keyboard()

    compass = gyro = accel = True
    sense.set_imu_config(compass, gyro, accel)

    yaw_offset = 72

    while display.loop_running():
        orientation = sense.get_orientation_radians()
        if orientation is None:
            pass

        pitch = orientation["pitch"]
        roll = orientation["roll"]
        yaw = orientation["yaw"]

        yaw_total = yaw + math.radians(yaw_offset)

        sin_y = math.sin(yaw_total)
        cos_y = math.cos(yaw_total)

        sin_p = math.sin(pitch)
        cos_p = math.cos(pitch)

        sin_r = math.sin(roll)
        cos_r = math.cos(roll)

        abs_roll = math.degrees(math.asin(sin_p * cos_y + cos_p * sin_r * sin_y))
        abs_pitch = math.degrees(math.asin(sin_p * sin_y - cos_p * sin_r * cos_y))

        model.rotateToZ(abs_roll)
        model.rotateToX(abs_pitch)
        model.rotateToY(math.degrees(yaw_total))
        model.draw()

        keypress = keyb.read()

        if keypress == 27:
            keyb.close()
            display.destroy()
            break
        elif keypress == ord('m'):
            compass = not compass
            sense.set_imu_config(compass, gyro, accel)
        elif keypress == ord('g'):
            gyro = not gyro
            sense.set_imu_config(compass, gyro, accel)
        elif keypress == ord('a'):
            accel = not accel
            sense.set_imu_config(compass, gyro, accel)
        elif keypress == ord('='):
            yaw_offset += 1
        elif keypress == ord('-'):
            yaw_offset -= 1


sensors()
time.sleep(1)
pi3d_model()
