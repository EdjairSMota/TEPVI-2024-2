void setup() {
    Serial.begin(9600); // Configura a taxa de dados em bauds
}
void loop() {
    for (int i = 0; i <= 10; i++) {
         Serial.println(i); // Envia o número sequencial
         delay(500);       // Aguarda 500 ms
     }
}
