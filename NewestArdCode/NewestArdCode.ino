#include <Servo.h> // motor control library


String serialDataIn;
String data[3];
int counter;
int motor_pwm;
int elevator_pwm;
int rudder_pwm;
int inbyte;

Servo Motor;
Servo Rudder;
Servo Elevator;


void setup(){
  Serial.begin(9600);
  counter = 0;
  serialDataIn = String("");
  
  Motor.attach(11);
  Rudder.attach(9);
  Elevator.attach(10);
}


void readfromPI()
{
    inbyte = Serial.read();
    if(inbyte >= '0' & inbyte <= '9')
      serialDataIn += inbyte;
    if (inbyte == ','){  // Handle delimiter
      data[counter] = String(serialDataIn);
      serialDataIn = String("");
      counter = counter + 1;
    }
    if(inbyte ==  '\r'){  // end of line
      motor_pwm= data[0].toInt();
      elevator_pwm= data[1].toInt();
      //rudder_pwm = data[2].toInt;
    }
}


void loop() 
{ 
    Motor.write(motor_pwm);              // tell servo to go to position in variable 'pos' 
    Elevator.write(elevator_pwm);
    Rudder.write(rudder_pwm);
} 
