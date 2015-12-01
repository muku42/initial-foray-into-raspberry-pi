# initial-foray-into-raspberry-pi

This is my Initial foray into Python programming using a Raspberry Pi 2 and an Astro Pi Sense HAT.

## About this repository

This repository was created to familiarize myself not only with Python programming and the Raspberry Pi (in all its flavors) but also to become more familiar with the whole version tracking process; `fork` `clone` `add` `commit` `push`

## About the Astro Pi Sense HAT

British ESA astronaut [Tim Peake](https://twitter.com/astro_timpeake) is going to the International Space Station for 6 months at the end of 2015 and he is taking two [Raspberry Pi](https://www.raspberrypi.org/) computers to run experiments coded by participants in the [Astro Pi](http://astro-pi.org/) coding competition for UK schools.

The Sense HAT is the hardware attachment board mounted to the Rasberry Pi's on the ISS, and is available to the public through several avenues; [Pimoroni](https://shop.pimoroni.com/products/raspberry-pi-sense-hat), [Raspberry Pi Foundation Swag Store](http://swag.raspberrypi.org/products/raspberry-pi-sense-hat), [Newark/Element 14](http://www.newark.com/raspberry-pi/raspberrypi-sensehat/add-on-board-attiny88-astro-pi/dp/49Y7569), and [MCM Electronics](http://www.mcmelectronics.com/product/RASPBERRY-PI-2483095-/83-16980)

The Raspberry Pi Foundation have created a [Python API](https://pypi.python.org/pypi/sense-hat) to provide access to the board's LED matrix and sensors. See the documentation at [pythonhosted.org/sense-hat](http://pythonhosted.org/sense-hat/)

## What I'd Like to Accomplish: `Daring to Dream`

There are several avenues that I'd like to pursue with the Raspberry Pi/Sense HAT/Python combo at some point:

* Creating a Raspberry Pi weather station using the Sense HAT `Temperature` `Humidity` & `Pressure` sensors
* Using the `gyroscope` `accelerometer` & `magnetometer` of the Sense HAT's `IMU` (Intertial Measurement Unit) to control the movement of an actual physical object like a [Sphero](http://www.sphero.com/sphero), (or Sphero's new [BB-8](http://www.sphero.com/starwars)) as seen in this [YouTube video](https://www.youtube.com/watch?v=VHCP5A5jM4o)
* Again, using the Sense HAT's IMU to control movement, but this time, to control the movement of something like the `text scroll` of the Sense HAT matrix or the movement of the `squirrel` in Al Sweigart's [Squirrel Eat Squirrel](https://inventwithpython.com/pygame/chapter8.html) game
* Creating some sort of OpenCV project using the Raspberry Pi [Camera Module](https://www.raspberrypi.org/products/camera-module/) and `who knows?`

## Current Focus

Right now I'm working on using the Sense HAT's `IMU` to control the `pitch` `roll` & `yaw` of a 3D object (of my own creation or, at least, choosing) much like Serge Schneider's [Apollo-Soyuz demo.](https://github.com/astro-pi/apollo-soyuz)  It looks like I will need both a `.obj` file and a `.mtl` file to replace the Apollo-Soyuz model. 
