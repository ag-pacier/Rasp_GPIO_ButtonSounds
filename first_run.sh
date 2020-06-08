#!/bin/bash
sudo apt update && sudo apt dist-upgrade -y && sudo apt install python3-pip gstreamer1.0-tools python3-gpiozero -y
pip3 install playsound
mkdir /home/pi/sounds
echo "Check documentation at https://gpiozero.readthedocs.io/en/stable/recipes.html"
echo "Place MP3s or WAVs in /home/pi/sounds"
