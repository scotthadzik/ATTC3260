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

if grep -Fq "alias python='/usr/bin/python3'" $CONFIG
then
	echo '.bashrc has already been modified'
else
	echo "" >> $BASHRC
	echo "alias python='/usr/bin/python3'" >> $BASHRC 
	echo "alias pip=pip3" >> $BASHRC
	echo "Modified .bashrc"
fi



echo "Install complete, rebooting."
# reboot