import time
import numpy as np

ThermistorPin = 0;
Vo = 0
R1 = 10000 
logR2 = 0.0 
R2 = 0.0 
T = 0.0 
Tc = 0.0 
Tf = 0.0
c1 = 1.009249522e-03 
c2 = 2.378405444e-04
c3 = 2.019202697e-07



while True: 

  Vo = adc.(ThermistorPin)
  R2 = R1 * (1023.0 / (Vo - 1.0))
  logR2 = np.log(R2);
  T = (1.0 / (c1 + c2*logR2 + c3*logR2*logR2*logR2));
  Tc = T - 273.15;
  Tf = (Tc * 9.0)/ 5.0 + 32.0; 

  print("Temperature: ") 
  print(Tf)
  print(" F; ")
  print(Tc)
  print(" C") 
  time.sleep(0.5)

