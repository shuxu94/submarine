  String serialDataInOld;
  String serialDataInNew = "";
  char serialInput;

void setup(){
  Serial.begin(9600);
}

void loop(){
  serialDataInNew = "";
  readtoPI();
  Serial.println(serialDataInNew);
  serialDataInOld = serialDataInNew;
  delay(500);
}
  
void readtoPI(){
  while(Serial.available()){
    serialInput = Serial.read();
    serialDataInNew.concat(serialInput);
  }
    if(serialDataInNew == ""){
      serialDataInNew = serialDataInOld;
    }
}
