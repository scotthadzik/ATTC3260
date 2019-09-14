#!/bin/sh
# installer.sh will install the necessary packages to get the the raspberry pi electronic station running 
# basic functions

# Install packages
#apt-get update
#apt-get upgrade -y

#wget -o - https://packagecloud.io/headmelted/codebuilds/gpgkey| sudo apt-key add -
#sudo apt-get install code-oss


#apt-get install $PACKAGES -y
#pip install twython


## Enable Camera Interface
BASHRC="/home/pi/.bashrc"
echo "test" >> BASHRC



echo "Install complete, rebooting."
# reboot