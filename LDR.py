#https://www.tweaking4all.com/hardware/arduino/arduino-light-sensitive-resistor/



#define LDRpin1 7  // pin where we connect LDR and resistor
#define LDRpin2 8  // pin where we connect LDR and resistor

int LDRValue1 = 0; // result of reading the digital pin
int LDRValue2 = 0; // result of reading the digital pin

void setup() {
  Serial.begin(9600); // sets serial port for communication
}

void loop() {
  LDRValue1 = digitalRead(LDRpin1);// read the value from the LDR
  LDRValue2 = digitalRead(LDRpin2);// read the value from the LDR
  
  Serial.print(LDRValue1);         // print the LDR1 value to the serial port
  Serial.print(" ");               // print a space
  Serial.print(LDRValue2);         // print the LDR2 value to the serial port
  
  if((LDRValue1==1)&&(LDRValue2==1)) {
    Serial.print(" -> HIGH"); }
  else if ((LDRValue1==1)&&(LDRValue2==0)) {
    Serial.print(" -> MEDIUM"); }
  else if ((LDRValue1==0)&&(LDRValue2==0)) {
    Serial.print(" -> LOW"); }
    
  Serial.println(" lighting");
  
  delay(100);                    // wait a little
}
