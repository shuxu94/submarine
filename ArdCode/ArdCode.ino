#include <Servo.h> // motor control library

#define COMPXMIN -490.0// used to calibrate magnetometer readings into heading
#define COMPXMAX 55.0
#define COMPYMIN -328.0
#define COMPYMAX 140.0

#define MOTORMAX 1810 //less than max backward
#define MOTORMIN 1140 //less than max forward
//#define MOTORMAX 1900 //max backward
#define MOTORMID 1475 //stopped
//#define MOTORMIN 1050 //max forward
#define MOTORMAXCHANGE 2 //max angle change per cycle

#define RUDDERMAX 2200 //right
#define RUDDERMID 1400 //straight
#define RUDDERMIN 900 //left

#define ELEVATORMAX 2150
#define ELEVATORMID 1515
#define ELEVATORMIN 880

String serialDataIn;
char serialInput;

//String data[3];
//int counter;
int motor_pwm;
int elevator_pwm;
int rudder_pwm;
int motor_pwm_old = MOTORMID;
int elevator_pwm_old = ELEVATORMID;
int rudder_pwm_old = RUDDERMID;
//int inbyte;

Servo Motor;
Servo Rudder;
Servo Elevator;


void setup(){
  Serial.begin(9600);
//  counter = 0;
  serialDataIn = "";
  
  Motor.attach(11);
  Rudder.attach(9);
  Elevator.attach(10);
}


void loop() 
{ 
      serialDataIn = "";
      readfromPI();
      
    Serial.println(motor_pwm);
    Serial.println(elevator_pwm);
    Serial.println(rudder_pwm);
    delay(3000);
    
    Motor.write(motor_pwm);              // tell servo to go to position in variable 'pos' 
    Elevator.write(elevator_pwm);
    Rudder.write(rudder_pwm);

} 

void readfromPI()
{
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

    // printing out the string that has been received from serial in the format #,#,#
/*    if (serialDataIn != ""){
        Serial.println(serialDataIn);
    }
*/
    int commaIndex = serialDataIn.indexOf(',');
    int secondCommaIndex = serialDataIn.indexOf(',', commaIndex+1);
    
    String motorpwm = serialDataIn.substring(0, commaIndex);
    String elevatorpwm = serialDataIn.substring(commaIndex+1, secondCommaIndex);
    String rudderpwm = serialDataIn.substring(secondCommaIndex+1);
    
     motor_pwm= motorpwm.toInt();
     elevator_pwm= elevatorpwm.toInt();
     rudder_pwm = rudderpwm.toInt();     
     
     
     // if there is no new input (aka inputs are 0), then go back to old input
     if(motor_pwm == 0){
       motor_pwm = motor_pwm_old;
     }
     else{
       motor_pwm_old = motor_pwm;
     }
     
     if(elevator_pwm == 0){
       elevator_pwm = elevator_pwm_old;
     }
     else{
       elevator_pwm_old = elevator_pwm;
     }
     
     if(rudder_pwm == 0){
       rudder_pwm = rudder_pwm_old;
     }
     else{
       rudder_pwm_old = rudder_pwm;
     }
     
}


