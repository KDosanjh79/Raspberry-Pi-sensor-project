#https://www.tweaking4all.com/hardware/arduino/arduino-light-sensitive-resistor/
import time
import Adafruit_ADS1x15
adc = Adafruit_ADS1x15.ADS1115()


LDRValue1 = 0 # result of reading the digital 
ldrChannel = 1 # LDR pin decleration set to 1




while True:
    LDRValue1 = adc.read_adc(ldrChannel) #read the value from the LDR
    print(LDRValue1)    # print the LDR1 value to the serial port
    if (LDRValue1==1):
        print(" -> HIGH")
    else:
        print(" -> LOW")
    time.sleep(0.1)              

