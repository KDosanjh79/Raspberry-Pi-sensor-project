# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import mraa;
import time;
import math;
import sys;


B = 3975
tempMraa = mraa.I2c(0)
tempRead = temp.read()
resistance = (1023-tempRead)*10000.0/tempRead
temp = 1/(math.log(resistance/10000.0))/B+1/298.15

