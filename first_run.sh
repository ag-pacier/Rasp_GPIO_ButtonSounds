#!/bin/bash
sudo echo "deb http://vontaene.de/raspbian-updates/ . main" >> /etc/apt/sources.list
sudo apt update && sudo apt dist-upgrade -y && sudo apt install gstreamer1.0 python3-gpiozero -y
pip3 install playsound
mkdir /home/pi/sounds
echo "Check documentation at https://gpiozero.readthedocs.io/en/stable/recipes.html"
echo "Place MP3s or WAVs in /home/pi/sounds"
