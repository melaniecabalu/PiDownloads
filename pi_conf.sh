#!/bin/bash

sudo apt-get update
sudo apt-get install build-essential python-dev python-smbus python-pip git
cd ~
git clone https://github.com/adafruit/Adafruit_Python_MPR121.git

cd Adafruit_Python_MPR121
sudo python setup.py install


