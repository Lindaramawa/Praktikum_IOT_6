void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode (2,INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int rain_sensor = digitalRead(2);
  if(rain_sensor==1)
  {
    Serial.println("Hujan");
    delay(500);
  }
  if(rain_sensor==0)
  {
    Serial.println("Tidak Hujan");
    delay(500);
  }
}
