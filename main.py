#!/bin/python3
#Main loop for button

from gpiozero import Button
from time import sleep
from playsound import playsound
from os import listdir
from os.path import isfile
from sys import exit
from random import choice

big_button = Button(21)
sound_loc = '/home/pi/sounds/'
valid_types = ('mp3', 'wav', 'MP3', 'WAV')
sounds = []

def find_sounds():
    ''' Hunt through sound_loc and list out all the valid sounds in the sounds list'''
    files = listdir(sound_loc)
    for file in files:
        if isfile(sound_loc + file):
            if file[:-3] in valid_types:
                sounds.append(file)
    if len(sounds) <= 0:
        exit("No sounds located at " + sound_loc)


def play_sound():
    '''randomly pick a sound from the valid sounds list and play it'''
    sound = choice(sounds)
    playsound(sound_loc + sound)


if __name__ == "__main__":
    #If run, make the list of sounds and play a sound every time the button is pressed
    find_sounds
    big_button.when_pressed = play_sound
    pause()