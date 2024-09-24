int val;
float temp;
char line[30];
void setup() {
  analogReference(INTERNAL);  // 1.1V para o ATmega328P
                              // tensão de referência para entradas analógicas
  Serial.begin (9600);
  while (!Serial) {;}         // espera a inicialização completa da biblioteca serial
}
void loop() {
  if (Serial.available()) {
    Serial.readStringUntil('\n').toCharArray(line,30);
    if (strstr(line,"A0?")==line) {
      val=analogRead(0); 
      Serial.print("A0 "); Serial.println(val);
    } else if (strstr(line,"A1?")==line) {
      val=analogRead(1); 
      Serial.print("A1 "); Serial.println(val);    
    } else if (strstr(line,"T?")==line) {
      temp=1.1*100*analogRead(0)/1023; 
      Serial.print("T "); Serial.println(temp);
    } else {
      Serial.println("unknown");
    }
  }
}


