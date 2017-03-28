# Raspberry-Pi-sensor-project
## Abstract (brief description of the project)

## Setting up the environment

### Preparing the installation of the raspbian 

### Installation of the mraa from repositories
PPA for installing on ubuntu: https://launchpad.net/~mraa/+archive/ubuntu/mraa

sudo add-apt-repository ppa:mraa/mraa

sudo apt-get update

sudo apt-get install libmraa1 libmraa-dev mraa-tools python-mraa python3-mraa


### Installation of the mraa from sources
Install Libraries
Install Dependencies

$ sudo apt update

$ sudo apt update will update your local cache of all currently available packages in the repository.

$ sudo apt install libpcre3-dev

$ sudo apt install git

$ sudo apt install cmake

$ sudo apt install python-dev
$ sudo apt install swig

Build and Install mraa

libmraa is not in apt so we’ll have to compile it from source. Don’t worry, it’s easy:

$ git clone https://github.com/intel-iot-devkit/mraa.git

$ mkdir mraa/build && cd $_

$ cmake .. -DBUILDSWIGNODE=OFF

$ make

$sudo make install

$ cd

That DBUILDSWIGNODE flag turns off node.js support, which isn’t available in the version of swig in apt. If you need node.js, you can compile a newer version of swig from source (3.01+).
Update Shared Library Cache

To use the library in C or C++ programs, we need to add it to our shared library cache. With root (or using “sudo”), open up the ld.so.conf file:

$ nano /etc/ld.so.conf

Scroll down to the bottom of the file and add:

/usr/local/lib/i386-linux-gnu/

Save and exit (‘Crtl-x’ and ‘y’ with nano). Type the command (using root or “sudo”):

$ sudo ldconfig

You can check to make sure that the cache was updated by typing the command:

$ ldconfig -p | grep mraa

Export Library Path for Python

If you plan to use Python with mraa, you will need to export its location to the Python path. Enter the command:

export PYTHONPATH=$PYTHONPATH:$(dirname $(find /usr/local -name mraa.py))

Note that this command lets us use the mraa module for this terminal session only. If we restart the Edison, we will have to retype the command.

Optional: You can modify the .bashrc file to run the commands automatically every time the Edison starts. Open the .bashrc file with your favorite editor. For example:

$ nano ~/.bashrc

Scroll all the way down to the bottom of the file, and add the command from above in a new line.

export PYTHONPATH=$PYTHONPATH:$(dirname $(find /usr/local -name mraa.py))

Updating Sudoers File

This part is also optional. If you installed sudo, you might notice that PYTHONPATH is not updated properly when you try to run a Python script with “sudo.” For example, you might get an error like “ImportError: No module named mraa.”

Open up the sudoers file:

$ sudo visudo

Right under the first “Defaults” line, add the following:

Defaults        env_keep += PYTHONPATH

Using Python

For Python, use your favorite text editor to create this simple script, called something like blink.py. For example:

$ nano blink.py

In that file, enter the following:

import mraa
import time


x = mraa.Gpio(31)
x.dir(mraa.DIR_OUT)

while True:
    x.write(1)
    time.sleep(0.5)
    x.write(0)
    time.sleep(0.5)

Save and exit the file (if you are using nano, press ‘Crtl-X’ and ‘y’).

Run it with:

$ python blink.py

retrieved from https://learn.sparkfun.com/tutorials/installing-libmraa-on-ubilinux-for-edison
## Author

## Tutors
Dr. Kofi Appiah <kofi.appiah@ntu.ac.uk>

Pedro Machado <pedro.baptistamachado@ntu.ac.uk>
