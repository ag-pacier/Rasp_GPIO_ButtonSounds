#!/bin/python3
#Main loop for button

from gpiozero import Button
from os import listdir
from os.path import join
from sys import exit
from random import choice
from signal import pause
from subprocess import run

big_button = Button(21)
sound_loc = '/home/pi/sounds/'

def find_sounds():
    ''' Hunt through sound_loc and list out all the valid sounds in the sounds list'''
    sounds = []
    for file in listdir(sound_loc):
        sounds.append(join(sound_loc, file))
    if len(sounds) <= 0:
        exit("No sounds located at " + sound_loc)
    else:
        return sounds


def play_sound():
    '''randomly pick a sound from the valid sounds list and play it'''
    sound = choice(find_sounds())
    run(['omxplayer', sound])
    print("Played: " + sound)


if __name__ == "__main__":
    #If run, make the list of sounds and play a sound every time the button is pressed
    big_button.when_pressed = play_sound
    pause()
