#include <Servo.h> // motor control library
#include <nmea.h> // GPS
#include <Wire.h> // compass
#include <OneWire.h> // temperature sensor
#include <stdlib.h>
#include <math.h>

NMEA GPS(GPRMC);
double GPSx,GPSy,Temp,Heading;
char compXStr [100];
char compYStr [100];
char GPSxstr [100];
char GPSystr [100];
char Tempstr [100];
char Headingstr [100];
int CompxMax,CompyMax,CompxMin,CompyMin;

// TEMPERATURE SENSOR SETUP CODE
int DS18S20_Pin = 2; //DS18S20 Signal pin on digital 2
OneWire ds(DS18S20_Pin); // on digital pin 2

//EXPENSIVE  SETUP
int compassAddress = 0x42 >> 1;
int reading = 0; 

int calibrating = 0;
int GetGPS = 0;

#define COMPXMIN -490.0// used to calibrate magnetometer readings into heading
#define COMPXMAX 55.0
#define COMPYMIN -328.0
#define COMPYMAX 140.0

#define MAXANGLE 180
#define MIDANGLE 90
#define MINANGLE 0


String serialDataIn;
char serialInput;

//String data[3];
//int counter;
int motor_angle;
int elevator_angle;
int rudder_angle;
int motor_angle_old = MIDANGLE;
int elevator_angle_old = MIDANGLE;
int rudder_angle_old = MIDANGLE;
//int inbyte;

Servo Motor;
Servo Rudder;
Servo Elevator;


void setup(){
  Serial.begin(9600); // PI
  Serial2.begin(4800); //gps
//  counter = 0;
  serialDataIn = "";
  
  Motor.attach(11);
  Rudder.attach(9);
  Elevator.attach(10);
}


void loop(){ 
  serialDataIn = "";
  readfromPI();
      
  Serial.println(motor_angle);
  Serial.println(elevator_angle);
  Serial.println(rudder_angle);

  delay(500);
    
//  motorwrite(motor_angle, motor_angle_old);
  Motor.write(motor_angle);              // tell servo to go to position in variable 'pwm' 
  Elevator.write(elevator_angle);
  Rudder.write(rudder_angle);

  motor_angle_old = motor_angle;
  elevator_angle_old = elevator_angle;
  rudder_angle_old = rudder_angle;
 /* 
  while(1){
    if(readGPS()){
      break;
    }    
  }
  */
  getTemp();
  sendInfo();


  if (Serial2.available()) Serial.write(Serial2.read());
} 

void readfromPI(){
/*    inbyte = Serial.read();
    if(inbyte >= '0' & inbyte <= '9')
      serialDataIn += char(inbyte);
    if (inbyte == ','){  // Handle delimiter
      data[counter] = String(serialDataIn);
      serialDataIn = String("");
      counter = counter + 1;
    }

      if(inbyte ==  '\r'){  // end of line
      motor_pwm= data[0].toInt();
      elevator_pwm= data[1].toInt();
      rudder_pwm = data[2].toInt();
    }
*/
    // takes in the input from serial and converts to string
    while(Serial.available()){
       serialInput = Serial.read();
       serialDataIn.concat(serialInput);
    }
//    Serial.println(serialDataIn);

    // printing out the string that has been received from serial in the format #,#,#
/*    if (serialDataIn != ""){
        Serial.println(serialDataIn);
    }
*/
    int commaIndex = serialDataIn.indexOf(',');
    int secondCommaIndex = serialDataIn.indexOf(',', commaIndex+1);
    
    String motorangle = serialDataIn.substring(0, commaIndex);
    String elevatorangle = serialDataIn.substring(commaIndex+1, secondCommaIndex);
    String rudderangle = serialDataIn.substring(secondCommaIndex+1);
    
     motor_angle= motorangle.toInt();
     elevator_angle= elevatorangle.toInt();
     rudder_angle = rudderangle.toInt();     
     
     
     // if there is no new input (aka inputs are 0), then go back to old input
     // if pwm is less than min or more than max, value will be changed to either min or max
     if(motor_angle == 0){
       motor_angle = motor_angle_old;
     }
     else{
       if(motor_angle <= MINANGLE){
         motor_angle = MINANGLE;
       }       
       if(motor_angle >= MAXANGLE){
         motor_angle = MAXANGLE;
       }
     }
     
     if(elevator_angle == 0){
       elevator_angle = elevator_angle_old;
     }
     else{
       if(elevator_angle <= MINANGLE){
         elevator_angle = MINANGLE;
       }
       if(elevator_angle >= MAXANGLE){
         elevator_angle = MAXANGLE;
       }
     }
     
     if(rudder_angle == 0){
       rudder_angle = rudder_angle_old;
     }
     else{
       if(rudder_angle <= MINANGLE){
         rudder_angle = MINANGLE;
       }
       if(rudder_angle >= MAXANGLE){
         rudder_angle = MAXANGLE;
       }
     }
     
}

void motorwrite(int new_angle, int old_angle){
  int angle = new_angle;
  if (new_angle > old_angle){
    while (angle > old_angle){
      if ((angle - old_angle) < 5){
        Motor.write(new_angle);
        return;
      }
      else{
        angle -= 5;
        Serial.println(angle);
        Motor.write(angle);
      }
      delay(500);
    }
  }
/*  
  if (new_angle < old_angle){
    while (angle < old_angle){
      if ((old_angle - angle) < 5){
        Motor.write(new_angle);
        return;
      }
      else{
        angle += 5;
        Motor.write(angle);
      }
      delay(500);
    }
  }
*/
}

int readGPS(){
  if(Serial2.available() > 0){
    char c = Serial2.read();
    if(GPS.decode(c)){
      if(GPS.gprmc_status()=='A'){
        GPSx=double(GPS.gprmc_latitude());
        GPSy=double(GPS.gprmc_longitude());
        Heading=double(GPS.gprmc_course())*PI/180;
        dtostrf(GPSx,20,10,GPSxstr);
        dtostrf(GPSy,20,10,GPSystr);
        dtostrf(Heading,20,10,Headingstr);
      }
      return 1;
    }
  }
  return 0;
}

int readCompass(int outputMode){
  byte magData[2];
  switch (outputMode)
  {
  case 0:
    Wire.beginTransmission(compassAddress);
    Wire.write(0x47);               // Write to RAM command
    Wire.write(0x4E);               // Output Mode control byte address
    Wire.write(0x00);               // 0x00 for Heading mode
    Wire.endTransmission();
    break;
  case 1:
    Wire.beginTransmission(compassAddress);
    Wire.write(0x47);               // Write to RAM command
    Wire.write(0x4E);               // Output Mode control byte address
    Wire.write(0x03);               // 0x03 for Magnetometer X mode
    Wire.endTransmission();
    break;
  case 2:
    Wire.beginTransmission(compassAddress);
    Wire.write(0x47);               // Write to RAM command
    Wire.write(0x4E);               // Output Mode control byte address
    Wire.write(0x04);               // 0x04 for Magnetometer Y mode
    Wire.endTransmission();
    break;
  default:
    Wire.beginTransmission(compassAddress);
    Wire.write(0x47);               // Write to RAM command
    Wire.write(0x4E);               // Output Mode control byte address
    Wire.write(0x00);               // default to Heading mode 
    Wire.endTransmission();
  }
  delayMicroseconds(100);        // RAM write needs 70 microseconds to respond

  Wire.beginTransmission(compassAddress);
  Wire.write("A");                     // The "Get Data" command
  Wire.endTransmission();
  delay(10);                    // Get Data needs 6 milliseconds to respond

  Wire.requestFrom(compassAddress, 2);  // Request the 2 byte data (MSB comes first)
  int i = 0;
  while(Wire.available() && i < 2)
  { 
    magData[i] = Wire.read();
    i++;
  }

int  magReading = magData[0]*256 + magData[1];
return magReading;
}

int getTemp(){ //returns the temperature from one DS18S20 in DEG Celsius
  byte data[12];
  byte addr[8];
  if ( !ds.search(addr)) { //no more sensors on chain, reset search
    ds.reset_search();
    return -1000;
  }
  if ( OneWire::crc8( addr, 7) != addr[7]) {
    Serial.println("CRC is not valid!");
    return -1000;
  }
  if ( addr[0] != 0x10 && addr[0] != 0x28) {
    Serial.print("Device is not recognized");
    return -1000;
  }
  ds.reset();
  ds.select(addr);
  ds.write(0x44,1); // start conversion, with parasite power on at the end
  byte present = ds.reset();
  ds.select(addr);  
  ds.write(0xBE); // Read Scratchpad
  for (int i = 0; i < 9; i++) { // we need 9 bytes
    data[i] = ds.read();
  }
  ds.reset_search();
  byte MSB = data[1];
  byte LSB = data[0];
  float tempRead = ((MSB << 8) | LSB); //using two's compliment
  float TemperatureSum = tempRead / 16;
  Temp=double(TemperatureSum);
  dtostrf(Temp,8,5,Tempstr);
  return 0;
}

int sendInfo(){ // OUTPUTS: 0=GPSx, 1=GPSy, 2=compx, 3=compy, 4=compz, 5=temp
  char sendstr[1000];
//  sprintf(sendstr,"%s %s %s %s %s",GPSxstr,GPSystr,compXStr,compYStr,Tempstr);
  sprintf(sendstr,"%s %s %s",GPSxstr,GPSystr,Tempstr);
  Serial.println(sendstr);
}

