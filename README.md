If you are doing this project from scratch, here are the products and files you can download to get your device to run just like ours

sudo pip3 install pvrhino  (This is for voice recognition)  
sudo pip3 install paho-mqtt    (MQTT communication with wristband)  
npm install express --save   (NPM)  
sudo pip3 install pvporcupinedemo    (Wake to speech recognition)  

If you would like to do more readings about specific modules, the authors, and how to use them, navigate to magicmirror --> modules --> then choose any module starting with the MMM- name

# Magic Mirror

First you will need a Rasperry Pi 3 or 4 and to connect that to a monitor. <br />
To install onto your own Pi manually: <br />
First you will need to have nodejs on your Pi (if you already have nodejs, skip this step): <br />
1) In Pi terminal: <br />
$ curl -sL https://deb.nodesource.com/setup_16.x | sudo -E bash -  <br />
$ sudo apt install -y nodejs <br />

3) Then install the smart mirror:  <br />
$ git clone https://github.com/180D-FW-2022/Team8.git  <br />
$ cd Team8 <br />
$ npm run install-mm <br />
4) To start enter command: <br />
$ npm run start <br />

And you are good to go!

# IMU Wristband

For the wristband, you will need a Raspberry Pi Zero, Berry IMU accelerometor/gyroscope, and battery source.

Download only the folder labeled 'imuWristbandPi' onto your raspberry pi zero. In that folder there is a file labeled 'imuPublisher.py'. Run that file with python 3 while the mirror is on, and you should be able to swile up to turn off the mirror, and swipe down to turn it back on.
