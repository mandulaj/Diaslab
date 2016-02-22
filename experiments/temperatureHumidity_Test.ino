#include <dht.h>
#define dht_apin A0

dht DHT;


void setup() {
  Serial.begin(9600);
  delay(500);
  Serial.println("DHT22 Humidity & temperature Sensor\n\n");
  delay(1000);
 
}
 
void loop(){
 
    DHT.read22(dht_apin);
    
    Serial.print("Humidity = ");
    Serial.print(DHT.humidity);
    Serial.print("%  ");
    Serial.print("Temperature = ");
    Serial.print(DHT.temperature); 
    Serial.println("C  ");
    
    delay(2500);
 
}// end loop() 
