#!/bin/bash
sudo apt update && sudo apt dist-upgrade -y && sudo apt install python3-pip omxplayer python3-gpiozero -y
mkdir /home/pi/sounds
sudo cp ./button_mon.service /etc/systemd/system/button_mon.service
sudo systemctl daemon-reload
sudo systemctl enable button_mon.service
echo "Place MP3s or WAVs in /home/pi/sounds and reboot"
