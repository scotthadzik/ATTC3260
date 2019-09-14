#!/bin/sh
# installer.sh will install the necessary packages to get the the raspberry pi electronic station running 
# basic functions

# Install packages
sudo apt update
sudo apt upgrade -y



#apt-get install $PACKAGES -y
#pip install twython


## Enable Camera Interface
BASHRC="/home/pi/.bashrc"

if grep -Fq "alias python='/usr/bin/python3'" $BASHRC
then
	echo '.bashrc has already been modified'
else
	echo "" >> $BASHRC
	echo "alias python='/usr/bin/python3'" >> $BASHRC 
	echo "alias pip=pip3" >> $BASHRC
	echo "Modified .bashrc"
fi


sudo wget -qO - https://packagecloud.io/headmelted/codebuilds/gpgkey | sudo apt-key add -;
SOURCES="/etc/apt/sources.list"

if grep -Fq "deb https://packagecloud.io/headmelted/codebuilds/raspbian/ jessie main" $SOURCES
then
	echo 'sources.list has already been modified'
else
	sudo bash -c 'echo "deb https://packagecloud.io/headmelted/codebuilds/raspbian/ jessie main" >> /etc/apt/sources.list' 
	echo "Modified sources.list"
fi

sudo apt update
sudo apt install code-oss -y

echo "Install complete, rebooting."
reboot