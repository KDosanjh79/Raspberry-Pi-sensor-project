# https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/using-a-pir

import time
import mraa
import Adafruit_ADS1x15
adc = Adafruit_ADS1x15.ADS1115()

LOW=0
HIGH=1
ledPin = mraa.Gpio(mraa.RASPBERRY_WIRING_PIN11)
ledPin.dir(mraa.DIR.OUT)               
inputPin = 2               
pirState = LOW            
val = 0                    
 

while True:
    val = adc.read.adc(inputPin)  
    if (val == LOW) and (pirState == LOW):
        print("NO Motion detected!")
        ledPin.write(LOW)
    else:
        print("Motion detected!");
        ledPin.write(HIGH)
        time.sleep(0.1)
        
  

