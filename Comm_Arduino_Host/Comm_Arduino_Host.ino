void setup() {
    Serial.begin(9600); 
    pinMode(13, OUTPUT); 
}
void loop() {
    if (Serial.available() > 0) { 
        String command = Serial.readStringUntil('\n');   
        if (command == "LED ON") {
          digitalWrite(13, HIGH); // Acende o LED
          Serial.println("LED is ON");
        } else if (command == "LED OFF") {
          digitalWrite(13, LOW); // Apaga o LED
          Serial.println("LED is OFF");
        } else {
            Serial.println(“Buguei!!!");
        }
    }
}