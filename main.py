#!/bin/python3
#Main loop for button

from gpiozero import Button
from playsound import playsound
from os import listdir
from sys import exit
from random import choice
from signal import pause

big_button = Button(21)
sound_loc = '/home/pi/sounds/'
valid_types = ('mp3', 'wav', 'MP3', 'WAV')
sounds = []

def find_sounds():
    ''' Hunt through sound_loc and list out all the valid sounds in the sounds list'''
    files = listdir(sound_loc)
    for file in files:
        if file[-3:] in valid_types:
            sounds.append(file)
    if len(sounds) <= 0:
        exit("No sounds located at " + sound_loc)


def play_sound():
    '''randomly pick a sound from the valid sounds list and play it'''
    sound = choice(sounds)
    playsound(sound_loc + sound)
    print("Played: " + sound)


if __name__ == "__main__":
    #If run, make the list of sounds and play a sound every time the button is pressed
    find_sounds
    big_button.when_pressed = play_sound
    pause()