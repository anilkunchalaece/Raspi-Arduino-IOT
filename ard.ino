void setup(){
Serial.begin(9600);
pinMode(9,OUTPUT);
}

void loop()
{
if(Serial.available())
{
  String inChar = Serial.readString();
if(inChar == "ON")
{
digitalWrite(9,HIGH);
Serial.println("LED is On...");
}else if(inChar == "OFF")
{
digitalWrite(9,LOW);
Serial.println("LED is Off...");
}else if(0 > inChar.toInt() < 1024)
{
  analogWrite(9,inChar.toInt());
  Serial.print("Led Brightness Value\t");
  Serial.println(inChar.toInt());
}
  
}//end of available
}//end of loop

