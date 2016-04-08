# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import sys		 # Library needed to use sys.exit(1) from line 14
import time		 # Library needed to use time.sleep(0.1) from line 72
import pygame	 # Library needed to play the piano sounds through the speaker
import Adafruit_MPR121.MPR121 as MPR121		# Library needed to use the functions necessary to interact with Touch Hat

print 'Adafruit MPR121 Capacitive Touch Audio Player Test'

# Create an instance of the Touch Hat called ‘cap’‐needed to interact with the hat in our code
cap = MPR121.MPR121()

# Checks if wiring between Touch Hat and Raspberry Pi is set up properly
if not cap.begin():
    print 'Error initializing MPR121.  Check your wiring!'
    sys.exit(1)

# Set the preset arguments for the audio mixer needed to play sounds      
# Parameters of pre_init(frequency, size, number_of_channels, buffer_size)
#	frequency - pitches of audio Ex. bass, treble, etc.
#	Size - how many bits used for each audio sample
#	Num_of_channels - In sound systems: 1) MONO - only 1 source of audio   2) STEREO - L/R audio
#	buffer_size - controls number of internal samples in mixer to handle delay of playing a recorded note
pygame.mixer.pre_init(44100, -16, 12, 512)
pygame.init()	# initialize the mixer for sound loading and playback


# pygame.mixer.Sound() creates a new Sound object from a .wav file (sound files)
# Sound object represents actual sound sample data
sounds = [pygame.mixer.Sound('/home/pi/A.wav'),
	pygame.mixer.Sound('/home/pi/B.wav'),
	pygame.mixer.Sound('/home/pi/D.wav'),
	pygame.mixer.Sound('/home/pi/E.wav'),
	pygame.mixer.Sound('/home/pi/F.wav'),
	pygame.mixer.Sound('/home/pi/G.wav')]

# Set volume for each sound
for i in range(6):
        sounds[i].set_volume(1)

# Main loop to print a message every time a pin is touched.
print 'Press Ctrl-C to quit.'

# Try-except, handles the error when exiting from the infinite loop
try:
	while True:
    # Checks 6 of the pins by calling the is_touched method 
	# with a pin number to directly check that pin.
		if cap.is_touched(0):
        		print 'Pin 0 is being touched!'
			sounds[0].play()
		
		if cap.is_touched(1):
			print 'Pin 1 is being touched!'
			sounds[1].play()

		if cap.is_touched(2):
			print 'Pin 2 is being touched!'
			sounds[2].play()
			
		if cap.is_touched(3):
			print 'Pin 3 is being touched!'
			sounds[3].play()
			
		if cap.is_touched(4):
			print 'Pin 4 is being touched!'
			sounds[4].play()
			
		if cap.is_touched(5):
			print 'Pin 5 is being touched!'
			sounds[5].play()

		#Delay so sounds don't muddle together	
		time.sleep(0.1)
		
except:
	print