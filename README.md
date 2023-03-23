If you are doing this project from scratch, here are the products and files you can download to get your device to run just like ours

sudo pip3 install pvrhino  (This is for voice recognition)  
sudo pip3 install paho-mqtt    (MQTT communication with wristband)  
npm install express --save   (NPM)  
sudo pip3 install pvporcupinedemo    (Wake to speech recognition)  

If you would like to do more readings about specific modules, the authors, and how to use them, navigate to magicmirror --> modules --> then choose any module starting with the MMM- name

# Magic Mirror

First you will need a Rasperry Pi 3 and to connect that to a monitor. Then you can download all the files to your pi and it should be able to run.



# IMU Wristband

For the wristband, you will need a Raspberry Pi Zero, Berry IMU accelerometor/gyroscope, and battery source.

Download only the folder labeled 'imuWristbandPi' onto your raspberry pi zero. In that folder there is a file labeled 'imuPublisher.py'. Run that file with python 3 while the mirror is on, and you should be able to swile up to turn off the mirror, and swipe down to turn it back on.
