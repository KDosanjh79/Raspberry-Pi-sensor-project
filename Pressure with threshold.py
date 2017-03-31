# https://learn.adafruit.com/force-sensitive-resistor-fsr/using-an-fsr



# FSR simple testing sketch. 
 
# Connect one end of FSR to power, the other end to Analog 0.
# Then connect one end of a 10K resistor from Analog 0 to ground 
 
import time
import Adafruit_ADS1x15
adc = Adafruit_ADS1x15.ADS1115()
 
fsrPin = 3;     # the FSR and 10K pulldown are connected to a3
fsrReading = 0     # the analog reading from the FSR resistor divider
 

while True:
    fsrReading = adc.read.adc(fsrPin)
    print("Analog reading = ")
    print(fsrReading)     # the raw analog reading
    if (fsrReading < 10): # We'll have a few threshholds, qualitatively determined
        print(" - No pressure")
    elif (fsrReading < 200):
        print(" - Light touch")
    elif (fsrReading < 500):
        print(" - Light squeeze")
    elif (fsrReading < 800):
        print(" - Medium squeeze")
    else:
        print(" - Big squeeze")
        time.sleep(0.1)

