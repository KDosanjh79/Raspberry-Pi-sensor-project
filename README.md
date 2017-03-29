# Raspberry-Pi-sensor-project
## Abstract (brief description of the project)

## Setting up the environment

### Preparing the installation of the raspbian 

### Installation of the mraa from repositories
PPA for installing on ubuntu: https://launchpad.net/~mraa/+archive/ubuntu/mraa

- $ sudo add-apt-repository ppa:mraa/mraa

- $ sudo apt update

- $ sudo apt install libmraa1 libmraa-dev mraa-tools python-mraa python3-mraa


### Installation of the mraa from sources
Install Libraries
Install Dependencies

- $ sudo apt update

- $ sudo apt update will update your local cache of all currently available packages in the repository.

- $ sudo apt install libpcre3-dev

- $ sudo apt install git

- $ sudo apt install cmake

- $ sudo apt install python-dev

- $ sudo apt install swig

Build and Install mraa

libmraa is not in apt so we’ll have to compile it from source. Don’t worry, it’s easy:

- $ git clone https://github.com/intel-iot-devkit/mraa.git

- $ mkdir mraa/build && cd $_

- $ cmake .. -DBUILDSWIGNODE=OFF

- $ make

- $ sudo make install

- $ cd ~

That DBUILDSWIGNODE flag turns off node.js support, which isn’t available in the version of swig in apt. If you need node.js, you can compile a newer version of swig from source (3.01+).
Update Shared Library Cache

To use the library in C or C++ programs, we need to add it to our shared library cache. With root (or using “sudo”), open up the ld.so.conf file:

- $ nano /etc/ld.so.conf

Scroll down to the bottom of the file and add:

``` 
/usr/local/lib/i386-linux-gnu/ 
```

Save and exit (‘Crtl-x’ and ‘y’ with nano). Type the command (using root or “sudo”):

- $ sudo ldconfig

You can check to make sure that the cache was updated by typing the command:

- $ ldconfig -p | grep mraa

Export Library Path for Python

If you plan to use Python with mraa, you will need to export its location to the Python path. Enter the command:

```
export PYTHONPATH=$PYTHONPATH:$(dirname $(find /usr/local -name mraa.py))
```

Note that this command lets us use the mraa module for this terminal session only. If we restart the Edison, we will have to retype the command.

Optional: You can modify the .bashrc file to run the commands automatically every time the Edison starts. Open the .bashrc file with your favorite editor. For example:

- $ nano ~/.bashrc

Scroll all the way down to the bottom of the file, and add the command from above in a new line.
```
export PYTHONPATH=$PYTHONPATH:$(dirname $(find /usr/local -name mraa.py))
```
Updating Sudoers File

This part is also optional. If you installed sudo, you might notice that PYTHONPATH is not updated properly when you try to run a Python script with “sudo.” For example, you might get an error like “ImportError: No module named mraa.”

Open up the sudoers file:

- $ sudo visudo

Right under the first “Defaults” line, add the following:
```
Defaults        env_keep += PYTHONPATH
```
Using Python

For Python, use your favorite text editor to create this simple script, called something like blink.py. For example:

- $ nano blink.py

In that file, enter the following:
```
import mraa
import time

# setup
x = mraa.Gpio(31)
x.dir(mraa.DIR_OUT)

# loop
while True:
    x.write(1)
    time.sleep(0.5)
    x.write(0)
    time.sleep(0.5)
```

Save and exit the file (if you are using nano, press ‘Crtl-X’ and ‘y’).

Run it with:

- $ python blink.py

retrieved from https://learn.sparkfun.com/tutorials/installing-libmraa-on-ubilinux-for-edison

## i2c configuration

Step 1: Download the latest Raspbian linux image and burn to your SD Card following the instructions on http://elinux.org/RPi_Easy_SD_Card_Setup

If you are using Raspian Linux 3.18 or later you need to go into the raspberry pi config utility and enable I2C.

sudo raspi-config

Select 8 Advanced Options and then  A7 I2C - Enable/Disable automatic loading. A prompt will appear asking Would you like the ARM I2C interface to be enabled?, select Yes, exit the utility and reboot your raspberry pi.

sudo reboot

Step 2: Next you need to update your Raspberry Pi to ensure all the latest packages are installed:

sudo apt-get update

sudo apt-get upgrade

sudo apt-get dist-upgrade

Step 3 a:  Once you have logged into your Raspberry Pi from the command line, run the following command to install SMBus and Python Dev:

sudo apt-get install python-smbus python3-smbus python-dev python3-dev

Step 4:  From the command line, run the following command to install i2c-tools:

sudo apt-get install i2c-tools

For previous releases before Raspian Linux 3.18 you need to complete the following steps:

Step 5: Enable I2C and SPI protocols. I2C and SPI protocols are turned off in the wheezy distro by default, so you will need to enable them by editing the file /etc/modprobe.d/raspi-blacklist.conf :

sudo nano /etc/modprobe.d/raspi-blacklist.conf

In the file you will see two lines, you need to disable the blacklisting of these by adding a # character before each line:

#blacklist spi-bcm2708

#blacklist i2c-bcm2708

Save your changes and exit the nano editor.

Step 6:

For recent versions of the Raspberry Pi (3.18 kernel or later) you will need to update the /boot/config.txt file.  Open the file with nano using the command:

sudo nano /boot/config.txt
Add the following text to the bottom of the file:

dtparam=i2c1=on
dtparam=i2c_arm=on
Save your changes and exit the nano editor.

All versions:

Step 7: Set the Raspberry Pi to start I2C automatically at boot by editing /etc/modules :

sudo nano /etc/modules

Use your cursor keys to move to the last line and add a new line and then add:

i2c-dev

Save your changes and exit the nano editor.

Step 8: To avoid having to run the I2C tools at root add the ‘pi’ user to the I2C group:

sudo adduser pi i2c

Step 9: Next reboot the Raspberry Pi:

sudo reboot

retrieved from : https://www.abelectronics.co.uk/kb/article/1/i2c--smbus-and-raspbian-linux

## Author

## Tutors
Dr. Kofi Appiah <kofi.appiah@ntu.ac.uk>

Pedro Machado <pedro.baptistamachado@ntu.ac.uk>
