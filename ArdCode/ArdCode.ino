#include <Servo.h> // motor control library


String serialDataIn;
char serialInput;

//String data[3];
//int counter;
int motor_pwm;
int elevator_pwm;
int rudder_pwm;
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
/*    
    Motor.write(motor_pwm);              // tell servo to go to position in variable 'pos' 
    Elevator.write(elevator_pwm);
    Rudder.write(rudder_pwm);
*/
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

}


