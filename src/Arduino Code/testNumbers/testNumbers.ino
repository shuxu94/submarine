char sendstr [100] = "50 60 70 80 90";

void setup(){
  Serial.begin(9600);
}

void loop(){
  Serial.println(sendstr);
  delay(500);
}
