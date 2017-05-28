#!/bin/sh 
sudo apt-get install python3-pip
sudo pip install selenium
sudo pip install uuid


//To install MQTT for Python install below 
pip install paho-mqtt 
sudo wget http://repo.mosquitto.org/debian/mosquitto-repo.gpg.key 
sudo apt-key add mosquitto-repo.gpg.key 
cd /etc/apt/sources.list.d/ 
sudo wget http://repo.mosquitto.org/debian/mosquitto-jessie.list 
sudo apt-get update 
sudo apt-get install mosquito 
sudo apt-get install mosquitto mosquitto-clients python-mosquito 
sudo /etc/init.d/mosquitto stop 
